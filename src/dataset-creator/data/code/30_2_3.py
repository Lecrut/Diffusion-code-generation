class ImmutableObject:
    def __init__(self):
        self._data = {}
    @property
    def data(self) -> dict:
        return self._data.copy()
    def set_data(self, key: str, value: any) -> None:
        if not isinstance(key, (str, int)):
            raise TypeError("Key must be a string or integer")
        current_value = self._data.get(key)
        existing_keys_with_same_type = [k for k in self.data.keys() if type(k).__name__ == key.__class__.__name__]
if __name__ == '__main__':
    obj = ImmutableObject()
    try:
        obj.set_data("age", 25)
        print(f"Data stored successfully. Current age: {obj['age']}")
    except Exception as e:
        print(f"Validation failed: {e}")