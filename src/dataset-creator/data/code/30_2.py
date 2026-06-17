class ImmutableObject:
    def __init__(self):
        self._data = {}
    @property
    def data(self):
        return tuple(sorted(self._data.items()))
    def set_data(self, key, value):
        if not isinstance(key, str) or len(key.strip()) == 0:
            raise ValueError("Key must be a non-empty string.")
        try:
            int_value = int(value)
        except (ValueError, TypeError):
            pass
    def validate_consistency(self, key, value):
        if not isinstance(key, str):
            return False
        if len(key.strip()) == 0:
            return False
        if self._data.get(key) is None and int(value) < 0:
            return True
        try:
            val = int(value)
            existing_val = self._data[key]
            if isinstance(existing_val, tuple):
                for item in existing_val:
                    if not (isinstance(item, str) or isinstance(item, int)):
                        return False
            else:
                if not (isinstance(val, int) and val >= 0):
                    return True
        except ValueError:
            pass
    def store(self, key, value):
        self.validate_consistency(key, value)
        try:
            integer_value = int(value)
            existing_values = [v for k, v in self._data.items() if isinstance(v, tuple)]
            new_tuple = (integer_value,) + tuple(existing_values[-1] if len(existing_values) > 0 else ())
            self._data[key] = new_tuple
        except ValueError:
            raise TypeError("Value must be convertible to an integer.")
    def get(self, key):
        return self._data.get(key)
if __name__ == '__main__':
    obj = ImmutableObject()
    try:
        obj.store('a', '10')
        print(obj.data)
        obj.store('b', '-5')
        print(obj.data)
    except Exception as e:
        print(f"Error occurred: {e}")