class StudentRecord:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major
class StudentDatabase:
    def __init__(self):
        self.students = {}
    def add_student(self, student):
        self.students[student.student_id] = student
    def view_all_students(self):
        return list(self.students.values())
    def view_student(self, student_id):
        return self.students.get(student_id)
    def delete_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False
if __name__ == '__main__':
    db = StudentDatabase()
    student1 = StudentRecord(101, "Alice Smith", "Computer Science")
    student2 = StudentRecord(102, "Bob Johnson", "Physics")
    student3 = StudentRecord(103, "Charlie Brown", "Mathematics")
    db.add_student(student1)
    db.add_student(student2)
    db.add_student(student3)
    print("--- All Students ---")
    for student in db.view_all_students():
        print(f"ID: {student.student_id}, Name: {student.name}, Major: {student.major}")
    print("\n--- Viewing Student 102 ---")
    student_view = db.view_student(102)
    if student_view:
        print(f"ID: {student_view.student_id}, Name: {student_view.name}, Major: {student_view.major}")
    else:
        print("Student not found")
    print("\n--- Deleting Student 101 ---")
    success = db.delete_student(101)
    if success:
        print("Student 101 deleted successfully.")
    else:
        print("Deletion failed, student not found.")
    print("\n--- All Students After Deletion ---")
    for student in db.view_all_students():
        print(f"ID: {student.student_id}, Name: {student.name}, Major: {student.major}")
    print("\n--- Viewing Deleted Student 101 ---")
    student_view = db.view_student(101)
    if student_view:
        print(f"ID: {student_view.student_id}, Name: {student_view.name}, Major: {student_view.major}")
    else:
        print("Student not found")