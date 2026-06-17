class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1.lower(), word2.lower()) if isinstance(word1, str) and isinstance(word2, str) else (word1, word2)
        combined_value = f"{word1} {word2}"
        self._data[key] = combined_value
    def get(self, word1: str, word2: str):
        key = (word1.lower(), word2.lower()) if isinstance(word1, str) and isinstance(word2, str) else (word1, word2)
        return self._data.get(key)
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add("Hello", "World")
    result = d.get("hello", "world")
    assert result == "Hello World"
    exit(0)