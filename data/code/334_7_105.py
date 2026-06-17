class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1, word2)
        combined = f"{word1}{word2}"
        if not isinstance(key, tuple):
            raise TypeError("Keys must be pairs of strings.")
        self._data[key] = combined
    def get(self, word1: str, word2: str) -> str | None:
        key = (word1, word2)
        return self._data.get(key) if isinstance(key, tuple) else None
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add("apple", "banana")
    d.add("cat", "dog")
    assert d.get("apple", "banana") == "applebanana"
    assert d.get("cat", "dog") == "catdog"
    print("All tests passed.")