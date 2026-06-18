from dataclasses import dataclass
@dataclass
class Person:
    name: str = ""
    age: int = 0
    email: str = ""
    def __post_init__(self):
        if not isinstance(self.name, str) or self.name.strip() == "":
            raise TypeError("Name must be a non-empty string.")
        if not isinstance(self.age, (int, float)) or self.age <= 0:
            raise ValueError("Age must be a positive integer.")
        if "@" not in self.email:
            raise ValueError("Email must contain an '@' symbol.")
if __name__ == '__main__':
    try:
        p = Person(name="Alice", age=25, email="alice@example.com")
        print(f"Created person: {p.name}, Age: {p.age}")
        try:
            bad_p = Person(age=-1)
        except ValueError as e:
            print(f"Catch error for negative age: {e}")
    except Exception as ex:
        print(f"Initialization failed due to validation errors.")