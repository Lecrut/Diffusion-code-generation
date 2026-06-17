import json
from typing import List, Dict
class Student:
    def __init__(self, name: str):
        self._name = name
    @property
    def name(self) -> str:
        return self._name
class StudentManager:
    def __init__(self):
        self._students: List[Student] = []
    def add_student(self, student_name: str) -> None:
        if not isinstance(student_name, str):
            raise TypeError("Name must be a string")
        new_student = Student(student_name)
        self._students.append(new_student)
    def get_all_names(self) -> List[str]:
        return [student.name for student in self._students]
def main():
    manager = StudentManager()
    sample_data = ["Alice", "Bob", "Charlie"]
    for name in sample_data:
        manager.add_student(name)
    names_list = manager.get_all_names()
    output_json = json.dumps(names_list, indent=2)
    print(output_json)
if __name__ == '__main__':
    main()