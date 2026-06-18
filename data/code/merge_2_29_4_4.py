class StudentManager:
    def __init__(self):
        self.students = []
    def add_student(self, name, age):
        self.students.append({"name": name, "age": age})
    def display_all_students(self):
        for student in self.students:
            print(f"{student['name']} ({student['age']})")
if __name__ == '__main__':
    manager = StudentManager()
    manager.add_student("Alice", 20)
    manager.add_student("Bob", 21)
    manager.display_all_students()