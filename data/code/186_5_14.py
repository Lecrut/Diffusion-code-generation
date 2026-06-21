class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def __repr__(self):
        return f"{self.name}: {self.grade}"

def sort_students(students):
    sorted_students = sorted(students, key=lambda student: student.grade)
    return sorted_students

if __name__ == '__main__':
    students = [
        Student("Alice", 85),
        Student("Bob", 92),
        Student("Charlie", 78),
        Student("David", 88)
    ]
    sorted_students = sort_students(students)
    print(sorted_students)