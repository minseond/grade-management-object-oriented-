class Student:
    def __init__(self, student_id, name, english_score, c_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.c_score = c_score
        self.python_score = python_score
        self.rank = None  # 등수 초기화
        self.calculate_total_and_average()
        self.calculate_grade()

    def calculate_total_and_average(self):
        self.total_score = self.english_score + self.c_score + self.python_score
        self.average = self.total_score / 3

    def calculate_grade(self):
        if self.average >= 90:
            self.grade = 'A'
        elif self.average >= 80:
            self.grade = 'B'
        elif self.average >= 70:
            self.grade = 'C'
        elif self.average >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

    def __str__(self):
        return f"{self.student_id} {self.name} ENG:{self.english_score} C:{self.c_score} PYTHON:{self.python_score} TOTAL:{self.total_score} AVG:{self.average:.2f} GRADE:{self.grade} RANK:{self.rank}"

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def calculate_ranks(self):
        sorted_students = sorted(self.students, key=lambda x: x.total_score, reverse=True)
        for index, student in enumerate(sorted_students):
            student.rank = index + 1

    def display_all_students(self):
        for student in sorted(self.students, key=lambda x: x.rank):
            print(student)

    def count_students_above_80(self):
        return sum(1 for s in self.students if s.average >= 80)

def input_student_info():
    student_id = input("Enter student ID: ")
    name = input("Enter name: ")
    english_score = int(input("Enter English score: "))
    c_score = int(input("Enter C language score: "))
    python_score = int(input("Enter Python score: "))
    return Student(student_id, name, english_score, c_score, python_score)

def main():
    manager = StudentManager()

    for _ in range(5):  # 5명의 학생 정보를 입력받음
        student = input_student_info()
        manager.add_student(student)

    manager.calculate_ranks()  # 등수 계산
    manager.display_all_students()  # 모든 학생 정보 출력 (등수 포함)

    # 80점 이상 학생 수 출력
    print("Number of students with average above 80:", manager.count_students_above_80())

if __name__ == "__main__":
    main()
