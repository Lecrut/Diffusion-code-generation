class SimpleObject:
    def __init__(self):
        self._data = {}
    @property
    def name(self):
        return self._data.get('name')
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise TypeError("Name must be a non-empty string.")
        self._data['name'] = value
    @property
    def age(self):
        return self._data.get('age')
    @age.setter
    def age(self, value):
        try:
            int_value = int(value)
            if not (0 <= int_value <= 150):
                raise ValueError("Age must be between 0 and 150.")
            self._data['age'] = int_value
        except TypeError as e:
            raise TypeError(f"Invalid age type. Expected integer, got {type(value).__name__}.") from e
    @property
    def email(self):
        return self._data.get('email')
    @email.setter
    def email(self, value):
        if not isinstance(value, str) or '@' not in value:
            raise ValueError("Email must be a valid string containing an '@'.")
        self._data['email'] = value
    def __repr__(self):
        return f"SimpleObject(name={self.name}, age={self.age}, email={self.email})"
if __name__ == '__main__':
    obj1 = SimpleObject()
    try:
        obj1.name = "Alice"
        obj1.age = 30
        obj1.email = "alice@example.com"
        print("Valid Object:", repr(obj1))
        try:
            obj2 = SimpleObject()
            obj2.name = "Bob"
            obj2.age = 30.5
            obj2.email = "bob@test.com"
        except TypeError as e:
            print("Caught Type Error for invalid age:", str(e))
        try:
            obj1.email = "invalid-email-format"
        except ValueError as e:
            print("Caught Value Error for invalid email:", str(e))
    except Exception as ex:
        print(f"Unexpected error occurred: {ex}")