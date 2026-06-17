class Person:
    def __init__(self):
        self._data = {}
    @property
    def name(self):
        return self._data.get('name')
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._data['name'] = value.strip()
    @property
    def age(self):
        return self._data.get('age')
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Age must be a positive integer.")
        self._data['age'] = value
    @property
    def email(self):
        return self._data.get('email')
    @email.setter
    def email(self, value):
        if not isinstance(value, str) or '@' not in value:
            raise ValueError("Email must be a valid string containing an '@'.")
        self._data['email'] = value.strip()
if __name__ == '__main__':
    person = Person()
    try:
        person.name = "Alice"
        person.age = 30
        person.email = "alice@example.com"
        print(f"Name: {person.name}")
        print(f"Age: {person.age}")
        print(f"Email: {person.email}")
    except ValueError as e:
        print(e)
    try:
        person.age = -5
    except ValueError as e:
        print("Caught expected error:", e)
    try:
        person.name = ""
    except ValueError as e:
        print("Caught expected error:", e)