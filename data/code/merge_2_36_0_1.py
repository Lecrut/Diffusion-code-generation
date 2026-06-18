class DictionaryLookup:
    def __init__(self):
        self._data = {}
    def set(self, key, value):
        if not isinstance(key, (str, int, float)):
            raise TypeError("Key must be a string or number")
        self._data[key] = value
    def get(self, key):
        return self._data.get(key)
    def contains(self, key):
        return key in self._data
if __name__ == '__main__':
    lookup = DictionaryLookup()
    lookup.set("apple", 10)
    lookup.set(42, "forty two")
    print(f"Value for 'apple': {lookup.get('apple')}")
    print(f"Value for 42: {lookup.get(42)}")
    print(f"Contains 'banana': {lookup.contains('banana')}")