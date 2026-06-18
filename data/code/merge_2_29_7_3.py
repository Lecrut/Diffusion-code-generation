from dataclasses import dataclass
@dataclass
class Student:
    name: str
    def to_dict(self) -> dict:
        return {"name": self.name}
    @classmethod
    def from_dict(cls, data: dict):
        if "name" not in data or isinstance(data["name"], list):
            raise ValueError("Invalid student data")
        instance = cls.__new__(cls)
        object.__setattr__(instance, "name", data["name"])
        return instance
if __name__ == '__main__':
    alice = Student(name="Alice Smith")
    bob = Student(name="Bob Jones")
    students_list = [alice, bob]
    serialized_data = []
    for student in students_list:
        d = student.to_dict()
        serialized_data.append(d)
    deserialized_students = [Student.from_dict(s) for s in serialized_data]
    print(f"Original names: {[s.name for s in students_list]}")
    print(f"Deserialized names: {[s.name for s in deserialized_students]}")