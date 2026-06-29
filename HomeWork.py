class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'
        if course not in self.courses_in_progress or course not in lecturer.courses_attached:
            return 'Ошибка'
        if course in lecturer.grades:
            lecturer.grades[course].append(grade)
        else:
            lecturer.grades[course] = [grade]
        return None

    def average_grade(self):
        if not self.grades:
            return 0.0
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return round(total / count, 1) if count else 0.0

    def __str__(self):
        avg = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses) if self.finished_courses else 'Нет'
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {avg}\n' \
               f'Курсы в процессе изучения: {courses_in_progress}\n' \
               f'Завершенные курсы: {finished}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() >= other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0.0
        total = sum(sum(grades) for grades in self.grades.values())
        count = sum(len(grades) for grades in self.grades.values())
        return round(total / count, 1) if count else 0.0

    def __str__(self):
        avg = self.average_grade()
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {avg}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() <= other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() != other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() >= other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if not isinstance(student, Student):
            return 'Ошибка'
        if course not in self.courses_attached or course not in student.courses_in_progress:
            return 'Ошибка'
        if course in student.grades:
            student.grades[course].append(grade)
        else:
            student.grades[course] = [grade]
        return None

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'

reviewer = Reviewer('Some', 'Buddy')
lecturer = Lecturer('Some', 'Buddy')
student = Student('Ruoy', 'Eman', 'your_gender')

student.courses_in_progress += ['Python', 'Git']
student.finished_courses += ['Введение в программирование']
lecturer.courses_attached += ['Python']
reviewer.courses_attached += ['Python']

reviewer.rate_hw(student, 'Python', 10)
reviewer.rate_hw(student, 'Python', 9)
reviewer.rate_hw(student, 'Python', 10)

student.rate_lecturer(lecturer, 'Python', 10)
student.rate_lecturer(lecturer, 'Python', 9)
student.rate_lecturer(lecturer, 'Python', 10)

print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecturer(lecturer, 'Python', 7))   # None
print(student.rate_lecturer(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecturer(lecturer, 'С++', 8))      # Ошибка
print(student.rate_lecturer(reviewer, 'Python', 6))   # Ошибка

print(lecturer.grades)  # {'Python': [7]}

lecturer2 = Lecturer('Another', 'Lecturer')
lecturer2.courses_attached += ['Python']
student.rate_lecturer(lecturer2, 'Python', 5)
student.rate_lecturer(lecturer2, 'Python', 6)

print(lecturer > lecturer2)
print(lecturer < lecturer2)

student2 = Student('Test', 'Student', 'M')
student2.courses_in_progress += ['Python']
reviewer.rate_hw(student2, 'Python', 7)
reviewer.rate_hw(student2, 'Python', 8)

print(student > student2)
print(student == student2)

print(reviewer)
print()
print(lecturer)
print()
print(student)

    def average_student_grade(students, course):
        total = 0
        count = 0
        for student in students:
            if course in student.grades:
                grades = student.grades[course]
                total += sum(grades)
                count += len(grades)
        return round(total / count, 1) if count else 0.0

    def average_lecturer_grade(lecturers, course):
        total = 0
        count = 0
        for lecturer in lecturers:
            if course in lecturer.grades:
                grades = lecturer.grades[course]
                total += sum(grades)
                count += len(grades)
        return round(total / count, 1) if count else 0.0
