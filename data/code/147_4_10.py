class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

def sort_students(students):
    return sorted(students, key=lambda student: student.grade, reverse=True)

if __name__ == '__main__':
    students = [Student('Alice', 85), Student('Bob', 92), Student('Charlie', 78)]
    sorted_students = sort_students(students)
    for student in sorted_students:
        print(f'{student.name}: {student.grade}')