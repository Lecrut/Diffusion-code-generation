class Student:
    def __init__(self, name):
        self.name = name
    def display(self):
        return f"Student Name: {self.name}"
def add_student(students_list, student_name):
    new_student = Student(student_name)
    students_list.append(new_student)
    return len(students_list) - 1
if __name__ == '__main__':
    sample_students = []
    index_0 = add_student(sample_students, "Alice")
    print(index_0)
    index_1 = add_student(sample_students, "Bob")
    print(index_1)
    index_2 = add_student(sample_students, "Charlie")
    print(index_2)
    for idx in range(len(sample_students)):
        if idx == 0:
            continue
        else:
            print(f"Student Name {idx}: ", end="")