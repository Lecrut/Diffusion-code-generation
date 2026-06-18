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
        except ValueError:
            raise TypeError("Value must be convertible to an integer.")
        if not isinstance(integer_value, int):
            return False
        else:
            self._data[key] = (integer_value,)
    def get(self, key):
        try:
            return self._data.get(key)
        except KeyError:
            pass
if __name__ == '__main__':
    obj = ImmutableObject()
    result1 = obj.set_data("a", "5")
    print(result1)
    result2 = obj.validate_consistency("b", "-3")
    print(result2)
    try:
        obj.store("c", "7")
        print(obj.get("c"))
    except Exception as e:
        pass