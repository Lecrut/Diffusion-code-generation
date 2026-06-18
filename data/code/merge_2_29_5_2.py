class StudentRegistry:
    def __init__(self):
        self.students = set()
    def add_student(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Invalid student name")
        original_name = name.strip().lower()
        existing_names = [s.lower().strip() for s in self.students]
        is_duplicate = any(original_name == e for e in existing_names)
        if not is_duplicate:
            self.students.add(name)
            return True
        return False
    def get_count(self):
        return len(self.students)
if __name__ == '__main__':
    registry = StudentRegistry()
    sample_students = [
        "Alice Johnson",
        "Bob Smith",
        "Charlie Brown",
        "alice johnson",                        
        "David Lee"
    ]
    for student in sample_students:
        result = registry.add_student(student)
        print(f"Added '{student}': {result}")
print(f"\nTotal students registered: {registry.get_count()}")