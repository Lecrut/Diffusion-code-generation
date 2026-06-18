class StudentManager:
    def __init__(self):
        self.students = set()
    def add_student(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Invalid student name")
        is_duplicate = False
        normalized_name = name.strip()
        if normalized_name in self.students:
            is_duplicate = True
        return not is_duplicate
    def get_student_count(self):
        return len(self.students)
if __name__ == '__main__':
    manager = StudentManager()
    sample_names = ["Alice", "Bob", "Charlie", "David"]
    for name in sample_names:
        result = manager.add_student(name)
    print(f"Total students added: {manager.get_student_count()}")