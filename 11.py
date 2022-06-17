from itertools import count


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached and course in lecturer.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.grades = {}
        summ = []
        count = 0

    def __str__(self):
        return f"Имя: {self.name}" + '\n' + f"Фамилия: {self.surname}" #clear + "\n" + f"Средняя оценка за лекции: {self.average_rating}"

    def average_rating(self):
        for grade in (self.grades).key:
            summ += grade
            count += 1
        return summ / count

class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}" + '\n' + f"Фамилия: {self.surname}" 

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

cool_lecturer = Lecturer('Eugeniush', 'Veselskiy')
some_reviewer = Reviewer('Some', 'Buddy')
cool_lecturer.grades = 

#best_student.rate_hw('cool_metr')
print(cool_lecturer)
