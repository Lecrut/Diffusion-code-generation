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
            raise ValueError("Grade level must be a number.")
        student = self.students[student_id]
        if student:
            old_grade = student["grade_level"]
            student["grade_level"] = int(new_grade)
            grade_change = new_grade - old_grade
            return {
                "success": True,
                "message": f"Grade updated for {student['name']} from {old_grade} to {new_grade}.",
                "change": grade_change
            }
        else:
            raise KeyError(f"No student found with ID '{student_id}'.")
    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            return {"success": True}
        raise ValueError("Student not found.")
    def list_all_students(self):
        return {sid: s for sid, s in sorted(self.students.items(), key=lambda x: int(x[1]['grade_level']))}
if __name__ == '__main__':
    manager = StudentManager()
    manager.add_student("S001", "Alice Johnson", 9)
    manager.add_student("S002", "Bob Smith", 8)
    manager.add_student("S003", "Charlie Davis", 7)
    manager.add_student("S004", "Diana Prince", 6)
    print("\n--- All Students ---")
    for sid, data in manager.list_all_students().items():
        print(f"ID: {sid}, Name: {data['name']}, Grade: {data['grade_level']}")
    update_result = manager.update_grade("S001", 8)
    if "success" in update_result:
        print(f"\n--- Update Result ---")
        for key, value in update_result.items():
            print(f"{key}: {value}")
    try:
        manager.remove_student("S999")
    except ValueError as e:
        print(f"\n--- Error Handling ---")
        print(e)
    final_list = manager.list_all_students()
    if len(final_list) == 3:
        print("\nFinal Student Count:", len(final_list))