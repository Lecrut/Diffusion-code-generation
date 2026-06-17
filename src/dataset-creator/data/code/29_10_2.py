class StudentManager:
    def __init__(self):
        self.students = []
    def add_student(self, name: str) -> None:
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Invalid student name")
        self.students.append({"name": name})
    def get_all_students(self) -> list[dict]:
        return [student.copy() for student in self.students]
if __name__ == '__main__':
    manager = StudentManager()
    sample_names = ["Alice", "Bob", "Charlie"]
    for name in sample_names:
        manager.add_student(name)
    output = manager.get_all_students()
    print(output)