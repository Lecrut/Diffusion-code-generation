class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1, word2)
        value = f"{word1}{word2}"
        if key in self._data and self._data[key] != value:
            raise ValueError(f"Duplicate or conflicting pair for {key}")
        self._data[key] = value
    def get(self, word1: str, word2: str) -> str:
        return self._data.get((word1, word2), None)
    def __contains__(self, key):
        if isinstance(key, tuple) and len(key) == 2:
            return (key[0], key[1]) in self._data
        raise TypeError("Key must be a pair of strings")
if __name__ == '__main__':
    d = WordPairDict()
    d.add("apple", "banana")
    assert d.get("apple", "banana") == "applebanana"
    print(d.get("apple", "banana"))