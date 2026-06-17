from dataclasses import dataclass
import json
@dataclass
class Student:
    name: str
    def to_dict(self):
        return {"name": self.name}
    @classmethod
    def from_dict(cls, data):
        return cls(name=data["name"])
if __name__ == '__main__':
    students = [Student("Alice"), Student("Bob")]
    serialized_data = json.dumps([s.to_dict() for s in students])
    print(serialized_data)