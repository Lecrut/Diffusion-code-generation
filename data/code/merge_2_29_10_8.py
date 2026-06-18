class Student:
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"Student Name: {self.name}")
def add_student(students_list, student_name):
    new_student = Student(student_name)
    students_list.append(new_student)
if __name__ == '__main__':
    student_data = []
    sample_names = ["Alice", "Bob", "Charlie"]
    for name in sample_names:
        add_student(student_data, name)
    print("All Students:")
    for i in range(len(student_data)):
        students_list_item = student_data[i]
        if isinstance(students_list_item, Student):
            students_list_item.display()