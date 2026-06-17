class StudentManager:
    def __init__(self):
        self.students = {}
    def add_student(self, student_id, name, grade_level):
        if not isinstance(student_id, int) and not (isinstance(student_id, str) and student_id.isdigit()):
            raise ValueError("Student ID must be a positive integer or numeric string.")
        key = int(student_id) if isinstance(student_id, str) else student_id
        self.students[key] = {
            "id": key,
            "name": name.strip(),
            "grade_level": grade_level,
            "enrolled_courses": []
        }
    def get_student(self, student_id):
        try:
            return self.students[int(student_id)] if isinstance(student_id, str) else self.students[student_id]
        except KeyError:
            raise ValueError(f"Student with ID {student_id} not found.")
if __name__ == '__main__':
    manager = StudentManager()
    manager.add_student(101, "Alice Johnson", 9)
    manager.add_student("205", "Bob Smith", 8)
    manager.add_student(304, "Charlie Davis", 7)
    print(f"Total students enrolled: {len(manager.students)}")
    alice = manager.get_student(101)
    print(f"\nStudent ID: {alice['id']}")
    print(f"Name: {alice['name']}")
    print(f"Grade Level: {alice['grade_level']}")
    bob = manager.get_student("205")
    print(f"\nStudent ID: {bob['id']}")
    print(f"Name: {bob['name']}")
    print(f"Grade Level: {bob['grade_level']}")