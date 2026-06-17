class EfficientDict:
    def __init__(self):
        self._data = {}
    def set(self, key, value):
        self._data[key] = value
    def get(self, key):
        return self._data.get(key)
    def contains(self, key):
        return key in self._data
if __name__ == '__main__':
    d = EfficientDict()
    d.set("apple", 10)
    d.set("banana", 20)
    print(d.get("apple"))