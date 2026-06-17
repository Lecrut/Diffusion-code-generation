class StudentManager:
    def __init__(self):
        self.students = {}
    def add_student(self, student_id, name, grade_level):
        if not isinstance(student_id, str) and len(student_id) > 0:
            raise ValueError("Student ID must be a non-empty string.")
        self.students[student_id] = {
            "name": name,
            "grade_level": int(grade_level),
            "enrolled_courses": []
        }
    def get_student(self, student_id):
        return self.students.get(student_id)
    def update_grade(self, student_id, new_grade):
        if not isinstance(new_grade, (int, float)):
            raise TypeError("Grade must be a number.")
        student = self.students[student_id]
        if student:
            old_grade = student["grade_level"]
            student["grade_level"] = int(new_grade)
            print(f"Grade updated for {student['name']} from {old_grade} to {int(new_grade)}")
    def remove_student(self, student_id):
        if student_id not in self.students:
            return False
        del self.students[student_id]
        return True
    def list_all_students(self):
        return [f"{sid}: {s['name']} (Grade {s['grade_level']})" for sid, s in self.students.items()]
if __name__ == '__main__':
    manager = StudentManager()
    manager.add_student("S001", "Alice Johnson", 9)
    manager.add_student("S002", "Bob Smith", 8)
    manager.add_student("S003", "Charlie Davis", 7)
    print("--- Current Student Roster ---")
    for line in manager.list_all_students():
        print(line)
    manager.update_grade("S001", 9.5)
    removed = manager.remove_student("S003")
    if not removed:
        print("Student S003 was already missing.")
    print("\n--- Updated Roster ---")
    for line in manager.list_all_students():
        print(line)