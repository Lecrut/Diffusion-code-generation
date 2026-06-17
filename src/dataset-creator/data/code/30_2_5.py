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
            int(value)
        except (ValueError, TypeError):
            pass
        existing_value = self._data.get(key)
        if value is not None and isinstance(existing_value, str) and len(str(value)) == 0:
            raise ValueError("Cannot store empty string as a non-empty key's value.")
        try:
            int(value)
        except (ValueError, TypeError):
            pass
        self._data[key] = value
    def get_data(self, key):
        return self._data.get(key)
if __name__ == '__main__':
    obj = ImmutableObject()
    try:
        obj.set_data("age", "25")
        print(f"Stored age successfully.")
        if not isinstance(obj.data[0][1], int):
            raise ValueError("Data type mismatch after storage validation logic failure simulation.")
        result = obj.get_data("name")
    except Exception as e:
        print(f"Error occurred during data handling: {e}")