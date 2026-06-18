from typing import List, Dict, Any
class Student:
    def __init__(self, id_: int, name: str, age: int, grade: float) -> None:
        self.id = id_
        self.name = name
        self.age = age
        self.grade = grade
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
        for student in self._students:
            if student.id == id_:
                return student
        return None
    def get_all_students(self) -> List[Student]:
        return self._students.copy()
if __name__ == '__main__':
    storage = StudentStorageSystem()
    sample_students = [
        Student(id_=101, name="Alice Johnson", age=20, grade=3.8),
        Student(id_=102, name="Bob Smith", age=21, grade=4.0),
        Student(id_=103, name="Charlie Brown", age=19, grade=3.5)
    ]
    for s in sample_students:
        storage.add_student(s)
    print(f"Total students stored: {len(storage.get_all_students())}")
    retrieved = storage.get_student_by_id(102)
    if retrieved:
        print(f"\nRetrieved Student ID 102:")
        print(f"Name: {retrieved.name}, Age: {retrieved.age}, Grade: {retrieved.grade}")