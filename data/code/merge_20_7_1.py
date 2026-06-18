class StudentDatabase:
    def __init__(self):
        self.students = {}
    def add_student(self, student_id, name, age) -> bool:
        if student_id in self.students:
            return False
        self.students[student_id] = {"name": name, "age": age}
        return True
    def view_student(self, student_id) -> dict or None:
        return self.students.get(student_id)
    def delete_student(self, student_id) -> bool:
        if student_id in self.students:
            del self.students[student_id]
            return True
        return False
if __name__ == '__main__':
    db = StudentDatabase()
    print("--- Adding Students ---")
    db.add_student(101, "Alice", 20)
    db.add_student(102, "Bob", 21)
    db.add_student(103, "Charlie", 19)
    print("\n--- Viewing Student (ID 102) ---")
    student102 = db.view_student(102)
    print(student102)
    print("\n--- Viewing Student (ID 999 - Non-existent) ---")
    student999 = db.view_student(999)
    print(student999)
    print("\n--- Deleting Student (ID 101) ---")
    success = db.delete_student(101)
    print(f"Deletion successful: {success}")
    print("\n--- Viewing Student (ID 101 after deletion) ---")
    student101 = db.view_student(101)
    print(student101)
    print("\n--- Final Database State ---")
    print(db.students)