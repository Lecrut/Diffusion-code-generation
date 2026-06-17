class DictionaryLookup:
    def __init__(self):
        self._table = {}
    def set(self, key, value):
        if isinstance(key, int) and not isinstance(value, (int, float)):
            raise TypeError("Value must be a number")
        self._table[key] = value
    def get(self, key):
        return self._table.get(key)
    def contains(self, key):
        return key in self._table
if __name__ == '__main__':
    d = DictionaryLookup()
    d.set(10, 5.234)
    d.set("apple", "red")
    print(d.get(10))
    print(d.contains("banana"))