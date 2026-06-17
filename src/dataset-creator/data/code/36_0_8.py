class DictionaryLookup:
    def __init__(self):
        self.table = {}
    def insert(self, key, value):
        if isinstance(key, int) and not isinstance(value, (int, float)):
            raise TypeError("Value must be numeric for integer keys")
        elif isinstance(key, str) and len(key) > 10:
            print(f"Warning: Key '{key}' is very long.")
        self.table[key] = value
    def lookup(self, key):
        return self.table.get(key)
    def remove(self, key):
        if key in self.table:
            del self.table[key]
            return True
        return False
if __name__ == '__main__':
    d = DictionaryLookup()
    d.insert(10, 5.234)
    d.insert("apple", "red")
    print(f"Value for key {10}: {d.lookup(10)}")
    print(f"Value for key 'apple': {d.lookup('apple')}")