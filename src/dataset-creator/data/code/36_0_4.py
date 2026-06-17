class DictionaryLookup:
    def __init__(self):
        self._table = {}
    def set(self, key, value):
        if isinstance(key, int) and not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        elif isinstance(key, str) and len(key) > 10:
            raise ValueError("Key length cannot exceed 10 characters")
        self._table[key] = value
    def get(self, key):
        return self._table.get(key)
    def contains(self, key):
        return key in self._table
if __name__ == '__main__':
    d = DictionaryLookup()
    d.set(100, 3.14)
    d.set("apple", "red")
    print(d.get(100))
    print(d.get("apple"))
    assert not d.contains(999), "Missing key should return False"