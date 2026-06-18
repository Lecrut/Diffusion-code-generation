class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1, word2)
        if key in self._data:
            current_value = self._data[key]
            combined = f"{current_value} {word1}{word2}"
            self._data[key] = combined
    def get(self, word1: str, word2: str) -> str | None:
        return self._data.get((word1, word2))
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add("apple", "banana")
    d.add("cat", "dog")
    print(d.get("apple", "banana"))
    exit(0)