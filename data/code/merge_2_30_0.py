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
            int_val = int(value)
            if not (0 <= int_val <= 150):
                raise ValueError("Age must be between 0 and 150.")
            self._data['age'] = int_val
        except TypeError as e:
            raise TypeError(f"Invalid type for age. Expected an integer, got {type(value).__name__}.") from e
    @property
    def email(self):
        return self._data.get('email')
    @email.setter
    def email(self, value):
        if not isinstance(value, str) or '@' not in value:
            raise TypeError("Email must be a valid non-empty string containing an '@'.")
        parts = value.split('@')
        if len(parts) != 2:
            raise ValueError("Invalid email format.")
        self._data['email'] = value
    def to_dict(self):
        return dict(self._data)
if __name__ == '__main__':
    obj1 = SimpleObject()
    try:
        obj1.name = "Alice"
        obj1.age = 25
        obj1.email = "alice@example.com"
        print("Valid Object:")
        data = obj1.to_dict()
        for k, v in data.items():
            if isinstance(v, int):
                print(f"{k}: {v}")
            else:
                print(f"{k}: {v}")
    except Exception as e:
        print(f"Error during initialization or setting attributes: {e}")
    obj2 = SimpleObject()
    try:
        obj2.name = "Bob"
        obj2.age = 30.5
    except TypeError as e:
        print(f"\nCaught expected error for invalid age type: {e}")
    try:
        pass
    except ValueError as e:
        print(f"Error caught here if we test out of bounds")