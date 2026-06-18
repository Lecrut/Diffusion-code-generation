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
        if type(existing_value).__name__ != type(value).__name__:
            raise TypeError(f"Type mismatch for key '{key}': expected {type(existing_value).__name__}, got {type(value).__name__}")
        self._data[key] = value
    def get_data(self, key):
        return self._data.get(key)
if __name__ == '__main__':
    obj = ImmutableObject()
    try:
        obj.set_data("Name", "Alice")
        print(f"Stored Name successfully.")
        if not isinstance(obj.data[0][1], str):
            raise ValueError("Data type mismatch detected in validation logic.")
    except Exception as e:
        print(f"Validation Error: {e}")