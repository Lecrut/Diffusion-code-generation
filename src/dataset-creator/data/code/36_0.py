class DictionaryLookup:
    def __init__(self):
        self._table = {}
    def set(self, key, value):
        if isinstance(key, int) and not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric for integer keys")
        elif isinstance(key, str) and len(key) > 10:
            print(f"Warning: Key '{key}' is very long.")
        self._table[key] = value
    def get(self, key):
        return self._table.get(key, None)
    def contains(self, key):
        return key in self._table
if __name__ == '__main__':
    d = DictionaryLookup()
    d.set(10, 3.5)
    d.set("apple", "red")
    print(d.get(10))
    print(d.get("banana"))