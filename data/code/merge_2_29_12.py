class StudentDataStore:
    def __init__(self):
        self.students = {}
    def add_student(self, student_id, name, grade_level, email):
        if not isinstance(student_id, str) and len(student_id) > 0:
            raise ValueError("Student ID must be a non-empty string.")
        self.students[student_id] = {
            "id": student_id,
            "name": name,
            "grade_level": grade_level,
            "email": email
        }
    def get_student(self, student_id):
        return self.students.get(student_id)
    def update_grade(self, student_id, new_grade):
        if not isinstance(new_grade, int) or new_grade < 1:
            raise ValueError("Grade level must be a positive integer.")
        student = self.students.get(student_id)
        if student is None:
            return False
        old_grade = student["grade_level"]
        student["grade_level"] = new_grade
        print(f"Updated grade for {student['name']} from {old_grade} to {new_grade}")
        return True
    def remove_student(self, student_id):
        if student_id not in self.students:
            raise KeyError("Student ID not found.")
        del self.students[student_id]
        print(f"Removed student with ID '{student_id}'.")
    def list_all_students(self):
        return {k: v for k, v in self.students.items()}
if __name__ == '__main__':
    store = StudentDataStore()
    sample_ids = ["S001", "S002", "S003"]
    names = ["Alice Johnson", "Bob Smith", "Charlie Brown"]
    grades = [9, 8, 7]
    emails = ["alice@example.com", "bob@example.com", "charlie@example.com"]
    for i in range(len(sample_ids)):
        store.add_student(
            student_id=sample_ids[i],
            name=names[i],
            grade_level=grades[i],
            email=emails[i]
        )
    print("\nInitial Student List:")
    data = store.list_all_students()
    for sid, info in data.items():
        print(f"ID: {sid}, Name: {info['name']}, Grade: {info['grade_level']}")
    result = store.update_grade("S001", 9)
    if not result:
        raise Exception("Update failed.")
    final_data = store.list_all_students()
    print("\nFinal Student List:")
    for sid, info in final_data.items():
        print(f"ID: {sid}, Name: {info['name']}, Grade: {info['grade_level']}")
    try:
        store.remove_student("S001")
    except KeyError as e:
        pass
    remaining = list(store.list_all_students().keys())
    print(f"\nRemaining Student IDs after removal: {remaining}")