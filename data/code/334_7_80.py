class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        if not isinstance(word1, str) or not isinstance(word2, str):
            raise TypeError("Both keys must be strings.")
        key = (word1.lower(), word2.lower())
        value = f"{word1} {word2}"
        self._data[key] = value
    def get(self, word1: str, word2: str) -> str | None:
        if not isinstance(word1, str) or not isinstance(word2, str):
            raise TypeError("Both keys must be strings.")
        key = (word1.lower(), word2.lower())
        return self._data.get(key)
    def contains(self, word1: str, word2: str) -> bool:
        if not isinstance(word1, str) or not isinstance(word2, str):
            raise TypeError("Both keys must be strings.")
        key = (word1.lower(), word2.lower())
        return key in self._data
    def __len__(self) -> int:
        return len(self._data)
if __name__ == '__main__':
    d = WordPairDict()
    d.add("Hello", "World")
    d.add("hello", "world")
    assert d.get("Hello", "World") is not None
    assert d.contains("HELLO", "WORLD")
    print(f"Total entries: {len(d)}")