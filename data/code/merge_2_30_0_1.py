from dataclasses import dataclass
@dataclass
class Person:
    name: str
    age: int
    email: str
    def __post_init__(self):
        if not isinstance(self.name, str) or self.name.strip() == "":
            raise TypeError("Name must be a non-empty string.")
        try:
            age = int(self.age)
            if age < 0:
                raise ValueError(f"Age cannot be negative. Got {self.age}.")
        except (ValueError, TypeError):
            raise TypeError("Age must be an integer representing years old.")
        if not isinstance(self.email, str) or "@" not in self.email:
            raise ValueError("Email must be a valid string containing '@'.")
if __name__ == '__main__':
    try:
        person = Person(name="Alice", age=30, email="alice@example.com")
        print(f"Person created successfully: {person.name}, Age: {person.age}")
    except Exception as e:
        print(f"Error creating Person object: {e}")