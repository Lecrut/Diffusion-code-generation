class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1, word2)
        if key in self._data:
            return
        combined = f"{word1}{word2}"
        self._data[key] = combined
    def get_combined(self, word1: str, word2: str) -> str | None:
        key = (word1, word2)
        if key in self._data:
            return self._data[key]
        return None
if __name__ == '__main__':
    d = WordPairDict()
    d.add("hello", "world")
    result = d.get_combined("hello", "world")
    assert result is not None and result == "helloworld"