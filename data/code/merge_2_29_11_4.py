import sys
class Student:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name
    def __repr__(self):
        return f"Student('{self.name}')"
class StudentManager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._students = []
        return cls._instance
    def add_student(self, student: Student):
        self._students.append(student)
    def get_all_students(self):
        return [s.name for s in self._students]
if __name__ == '__main__':
    manager = StudentManager()
    students_data = ["Alice", "Bob", "Charlie"]
    for name in students_data:
        student_obj = Student(name)
        manager.add_student(student_obj)
    print("Registered Students:")
    names_list = manager.get_all_students()
    if not names_list:
        sys.exit(0)
    for i, name in enumerate(names_list):
        print(f"{i + 1}. {name}")