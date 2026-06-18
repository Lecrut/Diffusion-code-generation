import json
from typing import List, Dict
class StudentRecord:
    def __init__(self, name: str):
        self._name = name
    @property
    def name(self) -> str:
        return self._name
    def to_dict(self) -> Dict[str, str]:
        return {"id": id(self), "name": self.name}
class StudentManager:
    _instance = None
    def __init__(self):
        if StudentManager._instance is not None:
            raise Exception("StudentManager already exists")
        self._records: List[Dict[str, str]] = []
    @classmethod
    def get_instance(cls) -> "StudentManager":
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    def add_student(self, name: str):
        self._records.append({"id": id(None), "name": name})
    def remove_student(self, student_id: int) -> bool:
        for i, record in enumerate(self._records):
            if record["id"] == student_id:
                del self._records[i]
                return True
        return False
    def get_all_students(self) -> List[Dict[str, str]]:
        return [r.copy() for r in self._records]
if __name__ == '__main__':
    manager = StudentManager.get_instance()
    manager.add_student("Alice")
    manager.add_student("Bob")
    manager.add_student("Charlie")
    students = manager.get_all_students()
    output_data = json.dumps(students, indent=2)
    print(output_data)