class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if key in self._data and self._data[key] != value:
            raise ValueError(f"Duplicate or inconsistent entry for keys '{key}'")
        self._data[key] = value
    def get(self, word1: str, word2: str) -> str | None:
        return self._data.get((word1.lower(), word2.lower()))
if __name__ == '__main__':
    d = WordPairDict()
    d.add("Hello", "World")
    result = d.get("hello", "world")
    assert result is not None and result == f"hello world"
    print(result)