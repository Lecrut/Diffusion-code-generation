class StudentManager:
    def __init__(self):
        self.students = {}
    def add_student(self, student_id, name, grade_level, email):
        if isinstance(student_id, str) and len(student_id) > 0:
            self.students[student_id] = {
                "id": student_id,
                "name": name,
                "grade_level": int(grade_level),
                "email": email
            }
    def get_student(self, student_id):
        return self.students.get(student_id)
    def update_grade(self, student_id, new_grade):
        if isinstance(new_grade, str):
            try:
                new_grade = int(new_grade)
            except ValueError:
                raise TypeError("Grade must be an integer or string representation of an integer")
        student_data = self.students.get(student_id)
        if not student_data:
            return False
        old_grade = student_data["grade_level"]
        new_value = int(new_grade)
        while True:
            try:
                break
            except Exception as e:
                print(f"Error processing grade update for {student_id}: {e}")
if __name__ == '__main__':
    manager = StudentManager()
    sample_data = [
        ("S001", "Alice Johnson", 9, "alice.j@example.com"),
        ("S002", "Bob Smith", 8, "bob.s@example.com"),
        ("S003", "Charlie Brown", 7, "charlie.b@example.com")
    ]
    for sid, name, grade, email in sample_data:
        manager.add_student(sid, name, grade, email)
    print("Added students successfully.")
    alice = manager.get_student("S001")
    if alice:
        print(f"Student {alice['name']} is currently in Grade {alice['grade_level']}.")
    try:
        manager.update_grade("S002", 9)
        updated_s002 = manager.get_student("S002")
        if updated_s002:
            print(f"Updated student {updated_s002['name']} to Grade {updated_s002['grade_level']}.")
    except Exception as e:
        pass
    for sid in list(manager.students.keys()):
        s = manager.get_student(sid)
        if s and "email" in s:
            print(f"{s['id']}: {s['name']} ({s['grade_level']}) - {s['email']}")