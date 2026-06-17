import json
from dataclasses import dataclass
@dataclass
class Student:
    name: str
    def to_dict(self) -> dict:
        return {"name": self.name}
    @classmethod
    def from_dict(cls, data: dict):
        if "name" not in data or not isinstance(data["name"], str):
            raise ValueError("Student must have a string 'name' attribute.")
        return cls(name=data["name"])
if __name__ == '__main__':
    student1 = Student(name="Alice")
    student2 = Student(name="Bob")
    data_list = [student1.to_dict(), student2.to_dict()]
    serialized_str = json.dumps(data_list)
    print("Serialized JSON:", serialized_str)
    deserialized_data = json.loads(serialized_str)
    restored_students = []
    for item in deserialized_data:
        if isinstance(item, dict):
            restored_student = Student.from_dict(item)
            restored_students.append(restored_student)
    print("Restored Students:", [s.name for s in restored_students])