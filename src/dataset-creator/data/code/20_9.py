class Student:
    def __init__(self, student_id, name, major, gpa):
        self.student_id = student_id
        self.name = name
        self.major = major
        self.gpa = gpa
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Major: {self.major}, GPA: {self.gpa}"
class StudentRecordManager:
    def __init__(self):
        self.students = {}
    def add_student(self, student):
        if student.student_id in self.students:
            raise ValueError("Student ID already exists")
        self.students[student.student_id] = student
    def get_student(self, student_id):
        return self.students.get(student_id)
    def find_all_students(self):
        return list(self.students.values())
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False
if __name__ == '__main__':
    manager = StudentRecordManager()
    student1 = Student(101, "Alice Smith", "Computer Science", 3.8)
    student2 = Student(102, "Bob Johnson", "Physics", 3.2)
    student3 = Student(103, "Charlie Brown", "Mathematics", 3.9)
    manager.add_student(student1)
    manager.add_student(student2)
    manager.add_student(student3)
    print("--- All Students ---")
    for student in manager.find_all_students():
        print(student)
    print("\n--- Retrieving Student 102 ---")
    retrieved_student = manager.get_student(102)
    if retrieved_student:
        print(retrieved_student)
    print("\n--- Attempting to retrieve non-existent student 999 ---")
    non_existent = manager.get_student(999)
    if non_existent is None:
        print("Student not found.")
    print("\n--- Deleting Student 101 ---")
    success = manager.delete_student(101)
    if success:
        print("Student 101 successfully deleted.")
    print("\n--- Updated List of Students ---")
    for student in manager.find_all_students():
        print(student)