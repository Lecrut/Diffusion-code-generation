class StudentRegistry:
    def __init__(self):
        self.students = set()
    def add_student(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise ValueError("Invalid student name")
        is_duplicate = False
        if name in self.students:
            is_duplicate = True
        if not is_duplicate:
            self.students.add(name)
    def get_count(self):
        return len(self.students)
if __name__ == '__main__':
    registry = StudentRegistry()
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    for name in sample_names:
        try:
            registry.add_student(name)
            print(f"Added {name}")
        except ValueError as e:
            print(f"Error adding {name}: {e}")
try:
    registry.add_student("Alice")
except Exception:
    pass                                                                                                                         
def add_student_secure(self, name):
    is_duplicate = False
    if name in self.students:
        print(f"Duplicate detected: {name}")
        return True
    self.students.add(name)
    return False