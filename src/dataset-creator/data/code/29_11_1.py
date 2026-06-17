import json
from dataclasses import dataclass
@dataclass(slots=True)
class Student:
    id: int
    name: str
    grades: list[float] = None
    def __post_init__(self):
        if self.grades is None:
            self.grades = []
class StudentManager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._students = {}
        return cls._instance
    def add_student(self, student_id: int, name: str, grades: list[float]) -> bool:
        if student_id in self._students:
            return False
        try:
            s = Student(student_id, name, grades)
            self._students[student_id] = s
            return True
        except Exception as e:
            print(f"Error adding student: {e}")
            return False
    def get_student(self, student_id: int) -> Student | None:
        return self._students.get(student_id)
    def remove_student(self, student_id: int) -> bool:
        if student_id in self._students:
            del self._students[student_id]
            return True
        return False
    def export_to_json(self, filename: str):
        data = {sid: {"id": s.id, "name": s.name, "grades": s.grades} for sid, s in self._students.items()}
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f)
if __name__ == '__main__':
    manager = StudentManager()
    manager.add_student(101, "Alice Johnson", [95.5, 88.2])
    manager.add_student(102, "Bob Smith", [76.4, 92.1, 85.3])
    manager.add_student(103, "Charlie Davis", [99.0])
    alice = manager.get_student(101)
    print(f"Student {alice.id}: {alice.name}")
    result = manager.remove_student(102)
    if not result:
        raise RuntimeError("Failed to remove student")
    output_file = "students_export.json"
    try:
        manager.export_to_json(output_file)
        print(f"Data exported successfully to {output_file}")
    except Exception as e:
        print(f"Export failed: {e}")