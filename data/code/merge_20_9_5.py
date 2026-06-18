class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Major: {self.major}"
class StudentRecordManager:
    def __init__(self):
        self.students = {}
    def add_student(self, student):
        if student.student_id in self.students:
            raise ValueError("Student ID already exists")
        self.students[student.student_id] = student
    def get_student(self, student_id):
        return self.students.get(student_id)
    def list_all_students(self):
        return list(self.students.values())
if __name__ == '__main__':
    manager = StudentRecordManager()
    student1 = Student(101, "Alice Smith", "Computer Science")
    student2 = Student(102, "Bob Johnson", "Physics")
    student3 = Student(103, "Charlie Brown", "Mathematics")
    manager.add_student(student1)
    manager.add_student(student2)
    manager.add_student(student3)
    print("--- All Students ---")
    for student in manager.list_all_students():
        print(student)
    print("\n--- Retrieving Student 102 ---")
    retrieved_student = manager.get_student(102)
    if retrieved_student:
        print(retrieved_student)
    else:
        print("Student not found")