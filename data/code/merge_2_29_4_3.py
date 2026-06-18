class Student:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Student({self.name})"
def initialize_students():
    students = []
    return students
def append_student(students, student_name):
    new_student = Student(student_name)
    students.append(new_student)
def iterate_students(students):
    for i in range(len(students)):
        yield (i + 1), students[i]
if __name__ == '__main__':
    all_students = initialize_students()
    append_student(all_students, "Alice")
    append_student(all_students, "Bob")
    append_student(all_students, "Charlie")
    print("Student List:")
    for index, student in iterate_students(all_students):
        print(f"{index}: {student}")