class DictionaryLookup:
    def __init__(self):
        self._table = {}
    def set(self, key, value):
        self._table[key] = value
    def get(self, key):
        return self._table.get(key)
if __name__ == '__main__':
    d = DictionaryLookup()
    d.set("apple", 10)
    d.set("banana", 20)
    print(d.get("apple"))