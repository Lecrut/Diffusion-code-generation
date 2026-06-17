class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if key in self._data and self._data[key] != value:
            raise ValueError("Value mismatch for existing key")
        self._data[key] = value
    def get(self, word1, word2):
        return self._data.get((word1.lower(), word2.lower()), None)
    def __repr__(self):
        return f"WordPairDict({dict(sorted(self._data.items()))})"
if __name__ == '__main__':
    d = WordPairDict()
    d.add("Hello", "World")
    d.add("HELLO", "WORLD")
    assert d.get("hello", "world") is not None
    print(d)