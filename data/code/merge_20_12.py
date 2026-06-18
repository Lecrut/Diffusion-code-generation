class StudentManager:
    def __init__(self):
        self.students = set()
    def add_student(self, name):
        self.students.add(name)
    def get_all_names(self):
        return list(self.students)
if __name__ == '__main__':
    manager = StudentManager()
    manager.add_student("Alice")
    manager.add_student("Bob")
    manager.add_student("Charlie")
    manager.add_student("Alice")
    print(manager.get_all_names())