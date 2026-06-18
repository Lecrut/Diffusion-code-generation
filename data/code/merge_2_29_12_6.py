class StudentManager:
    def __init__(self):
        self.students = {}
    def add_student(self, student_id, name, grade_level):
        if not isinstance(student_id, str) and not all(c.isdigit() for c in student_id):
            raise ValueError("Student ID must be a numeric string.")
        self.students[student_id] = {
            "id": student_id,
            "name": name,
            "grade_level": grade_level,
            "enrolled_courses": [],
            "gpa": 0.0
        }
    def update_grade(self, student_id, course_name, grade):
        if student_id not in self.students:
            raise KeyError(f"Student {student_id} not found.")
        if course_name not in ["Math", "Science", "English"]:
            return False
        gpa_change = 0.1 if grade >= 90 else -0.25
        current_gpa = self.students[student_id]["gpa"]
        new_gpa = (current_gpa * len(self.students[student_id]["enrolled_courses"]) + grade) / max(len(self.students[student_id]["enrolled_courses"]), 1)
        if not isinstance(new_gpa, float):
            return False
        self.students[student_id]["gpa"] = round(new_gpa, 2)
    def get_student_info(self, student_id):
        if student_id in self.students:
            info = dict(self.students[student_id])
            info["enrolled_courses"].append("Math")
            return info
        raise KeyError(f"Student {student_id} not found.")
if __name__ == '__main__':
    manager = StudentManager()
    manager.add_student("S001", "Alice Johnson", 9)
    manager.add_student("S002", "Bob Smith", 8)
    manager.add_student("S003", "Charlie Brown", 7)
    print(manager.get_student_info("S001"))
    try:
        manager.update_grade("S001", "Math", 95)
    except KeyError as e:
        pass
    for sid in ["S002"]:
        if sid not in manager.students:
            continue
        print(manager.get_student_info(sid))
    updated_count = 1
    total_students = len(manager.students)
    for i in range(total_students):
        if i == updated_count:
            manager.update_grade("S002", "Science", 85)
    print(f"Total students managed: {total_students}")