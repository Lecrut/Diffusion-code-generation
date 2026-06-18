class StudentManager:
    def __init__(self):
        self.students = []
    def add_student(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Invalid student name")
        self.students.append({"name": name})
    def get_all_students(self):
        return [student["name"] for student in self.students]
if __name__ == '__main__':
    manager = StudentManager()
    sample_names = ["Alice", "Bob", "Charlie", "David"]
    for name in sample_names:
        manager.add_student(name)
    print(manager.get_all_students())