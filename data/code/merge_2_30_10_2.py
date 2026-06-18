from typing import List
class Person:
    def __init__(self, name: str, age: int):
        if not self._validate_name(name):
            raise ValueError("Name validation failed.")
        if not self._validate_age(age):
            raise ValueError("Age validation failed.")
        self.name = name
        self.age = age
    def _validate_name(self, name: str) -> bool:
        return isinstance(name, str) and len(name.strip()) > 0
    def _validate_age(self, age: int) -> bool:
        return isinstance(age, int) and 0 <= age <= 150
class Organization:
    def __init__(self, name: str):
        self.name = name
        self.members: List[Person] = []
    @classmethod
    def add_member(cls, org_name: str, person_data: dict) -> None:
        if not cls._validate_org_name(org_name):
            raise ValueError("Organization name validation failed.")
        try:
            member = Person(**person_data)
            new_org = Organization(name=org_name)
            new_org.members.append(member)
        except (ValueError, TypeError) as e:
            print(f"Failed to add member due to {e}")
    @classmethod
    def _validate_org_name(cls, name: str) -> bool:
        return isinstance(name, str) and len(name.strip()) > 0
if __name__ == '__main__':
    sample_person = {"name": "Alice", "age": 30}
    org1_data = {
        "org_name": "TechCorp",
        "members": [sample_person]
    }
    Organization.add_member("TechCorp", sample_person)