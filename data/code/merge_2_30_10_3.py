class Person:
    def __init__(self, name: str, age: int):
        if not self._validate_name(name):
            raise ValueError("Name is required and must be a non-empty string.")
        if not isinstance(age, int) or age < 0:
            raise ValueError("Age must be a non-negative integer.")
        self.name = name
        self.age = age
    def _validate_name(self, name: str) -> bool:
        return len(name.strip()) > 0 and all(c.isalpha() for c in name.strip())
if __name__ == '__main__':
    person1 = Person("Alice", 30)
    print(f"Person created: {person1.name}, Age: {person1.age}")
    try:
        invalid_person = Person("", -5)
    except ValueError as e:
        print(f"Validation error caught: {e}")