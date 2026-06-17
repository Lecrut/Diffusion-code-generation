class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        if key not in self._data:
            combined = f"{key[0]} {key[1]}"
            self._data[key] = combined
        return self._data[key]
    def get(self, word1, word2):
        key = (word1.lower(), word2.lower())
        if key in self._data:
            return self._data[key]
        raise KeyError(f"Pair ({word1}, {word2}) not found")
if __name__ == '__main__':
    d = WordPairDict()
    d.add("hello", "world")
    result = d.get("Hello", "World")
    assert result == "hello world"
    exit(0)