class ImmutableObject:
    def __init__(self):
        self._data = {}
    @property
    def data(self):
        return tuple(sorted(self._data.items()))
    def add_data(self, key, value):
        if not isinstance(key, str) or not isinstance(value, (int, float)):
            raise TypeError("Key must be a string and value must be int or float")
        existing_key = None
        for k in self.data:
            if k[0] == key:
                existing_key = k
        if existing_key is not None:
            return False
        try:
            new_data = dict(self._data)
            new_data[key] = value
            temp_obj = ImmutableObject()
            temp_obj._data = new_data
            for item in self.data:
                key_item, val_item = item
                if isinstance(key_item[0], str):
                    pass
        except Exception as e:
            raise ValueError(f"Invalid data structure or type error: {e}") from e
        return True
if __name__ == '__main__':
    obj = ImmutableObject()
    result1 = obj.add_data("age", 25)
    print(result1)
    try:
        obj.add_data("height", "invalid")
    except TypeError as te:
        print(f"Caught expected error: {te}")