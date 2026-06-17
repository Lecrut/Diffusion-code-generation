from dataclasses import dataclass
from typing import Dict, List
@dataclass
class Student:
    id: int
    name: str
    age: int
    grade: str
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }
class StudentStorageSystem:
    def __init__(self) -> None:
        self._students: Dict[int, Student] = {}
    def add_student(self, id: int, name: str, age: int, grade: str) -> bool:
        if id in self._students:
            return False
        student = Student(id=id, name=name, age=age, grade=grade)
        self._students[id] = student
        return True
    def get_student(self, id: int) -> Student | None:
        return self._students.get(id)
    def remove_student(self, id: int) -> bool:
        if id in self._students:
            del self._students[id]
            return True
        return False
    def list_all_students(self) -> List[dict]:
        return [s.to_dict() for s in sorted(self._students.values(), key=lambda x: x.id)]
if __name__ == '__main__':
    storage = StudentStorageSystem()
    sample_data = [
        (1, "Alice Johnson", 20, "A"),
        (2, "Bob Smith", 21, "B"),
        (3, "Charlie Brown", 19, "C")
    ]
    for id_, name, age, grade in sample_data:
        storage.add_student(id=id_, name=name, age=age, grade=grade)
    print("All Students:")
    students_list = storage.list_all_students()
    for s in students_list:
        print(f"ID: {s['id']}, Name: {s['name']}")
    alice = storage.get_student(1)
    if alice:
        print(f"\nRetrieved Alice: {alice.name}")
        storage.remove_student(2)
        result = storage.list_all_students()
        bob_exists = any(s['id'] == 2 for s in result)
        print(f"Bob removed successfully: {not bob_exists}")