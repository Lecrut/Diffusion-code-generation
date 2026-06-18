class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, key1, key2):
        combined_key = (key1.lower(), key2.lower()) if isinstance(key1, str) and isinstance(key2, str) else (key1, key2)
        value = f"{key1} {key2}"
        self._data[combined_key] = value
    def get(self, key1, key2):
        combined_key = (key1.lower(), key2.lower()) if isinstance(key1, str) and isinstance(key2, str) else (key1, key2)
        return self._data.get(combined_key)
    def __repr__(self):
        return f"WordPairDict({dict(self._data)})"
if __name__ == '__main__':
    d = WordPairDict()
    d.add("hello", "world")
    d.add("HELLO", "WORLD")
    print(d.get("Hello", "World"))