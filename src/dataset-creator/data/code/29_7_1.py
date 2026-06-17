from dataclasses import dataclass
@dataclass
class Student:
    name: str
    def to_dict(self) -> dict:
        return {"name": self.name}
    @classmethod
    def from_dict(cls, data: dict):
        return cls(name=data["name"])
if __name__ == '__main__':
    student1 = Student("Alice")
    student2 = Student("Bob")
    students_list = [student1, student2]
    serialized_data = []
    for s in students_list:
        d = s.to_dict()
        serialized_data.append(d)
    print(f"Serialized data: {serialized_data}")
    restored_students = [Student.from_dict(s) for s in serialized_data]
    print("Restored names:", [s.name for s in restored_students])