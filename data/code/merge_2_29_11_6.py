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
    @classmethod
    def add_student(cls, name):
        student = Student(name)
        cls._students.append(student)
    @staticmethod
    def get_all_students():
        return [s.name for s in StudentManager._students]
if __name__ == '__main__':
    manager = StudentManager()
    sample_names = ["Alice", "Bob", "Charlie"]
    for name in sample_names:
        manager.add_student(name)
    print("Registered students:")
    for student_name in manager.get_all_students():
        print(f"  - {student_name}")