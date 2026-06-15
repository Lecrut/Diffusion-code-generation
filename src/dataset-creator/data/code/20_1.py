class StudentRegistry:
    def __init__(self):
        self.students = {}
    def add_student(self, name):
        self.students[name] = name
    def get_all_students(self):
        return list(self.students.keys())
if __name__ == '__main__':
    registry = StudentRegistry()
    registry.add_student("Alice")
    registry.add_student("Bob")
    registry.add_student("Charlie")
    print(registry.get_all_students())