class StudentRegistry:
    def __init__(self):
        self.students = set()
    def add_student(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Invalid student name")
        existing_names = [s for s in self.students]
        is_duplicate = any(s.lower().strip() == name.lower().strip() for s in existing_names)
        if is_duplicate:
            return False
        self.students.add(name.strip())
        return True
if __name__ == '__main__':
    registry = StudentRegistry()
    sample_data = [
        "Alice",
        "bob",
        "Charlie",
        "alice",                                           
        "David"
    ]
    for name in sample_data:
        result = registry.add_student(name)
        print(f"Added '{name}': {result}")