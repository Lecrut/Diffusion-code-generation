from typing import List, Dict, Any
class Student:
    def __init__(self, id_: int, name: str, grade_level: int) -> None:
        self.id = id_
        self.name = name
        self.grade_level = grade_level
class StudentStorageSystem:
    def __init__(self) -> None:
        self._students: List[Student] = []
    def add_student(self, student: Student) -> bool:
        for existing in self._students:
            if existing.id == student.id:
                return False
        self._students.append(student)
        return True
    def get_student_by_id(self, id_: int) -> Student | None:
        for s in self._students:
            if s.id == id_:
                return s
        return None
    def get_all_students(self) -> List[Student]:
        return list(self._students)
if __name__ == '__main__':
    storage = StudentStorageSystem()
    student_1 = Student(id_=1, name="Alice Johnson", grade_level=9)
    student_2 = Student(id_=2, name="Bob Smith", grade_level=8)
    student_3 = Student(id_=3, name="Charlie Brown", grade_level=7)
    storage.add_student(student_1)
    storage.add_student(student_2)
    if not storage.add_student(student_1):
        print("Duplicate ID detected.")
    found_alice = storage.get_student_by_id(1)
    all_students = storage.get_all_students()
    for s in all_students:
        print(f"ID: {s.id}, Name: {s.name}, Grade: {s.grade_level}")