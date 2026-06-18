class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
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
    student1 = Student(101, "Alice", 16, "A")
    student2 = Student(102, "Bob", 17, "B+")
    student3 = Student(103, "Charlie", 15, "A-")
    manager.add_student(student1)
    manager.add_student(student2)
    manager.add_student(student3)
    print("--- All Students ---")
    for student in manager.find_all_students():
        print(student)
    print("\n--- Finding Student 102 ---")
    student_found = manager.get_student(102)
    if student_found:
        print(student_found)
    else:
        print("Student not found")
    print("\n--- Deleting Student 101 ---")
    success = manager.delete_student(101)
    if success:
        print("Student 101 deleted successfully.")
    else:
        print("Deletion failed.")
    print("\n--- Students After Deletion ---")
    for student in manager.find_all_students():
        print(student)