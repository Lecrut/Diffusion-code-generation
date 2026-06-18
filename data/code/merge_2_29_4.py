class StudentManager:
    def __init__(self):
        self.students = []
    def add_student(self, name, age):
        self.students.append({"name": name, "age": age})
    def get_all_students(self):
        return self.students
if __name__ == '__main__':
    manager = StudentManager()
    manager.add_student("Alice", 20)
    manager.add_student("Bob", 21)
    for student in manager.get_all_students():
        print(f"{student['name']} ({student['age']})")