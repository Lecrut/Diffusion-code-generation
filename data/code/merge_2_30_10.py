class Person:
    def __init__(self, name: str, age: int):
        if not self._validate(name) or not self._validate(age):
            raise ValueError("Invalid data provided.")
        self.name = name
        self.age = age
    @staticmethod
    def _validate(value: any) -> bool:
        return value is not None and isinstance(value, (str, int))
if __name__ == '__main__':
    person1 = Person("Alice", 30)
    print(f"Name: {person1.name}, Age: {person1.age}")