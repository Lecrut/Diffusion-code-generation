class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1.lower(), word2.lower()) if isinstance(word1, str) and isinstance(word2, str) else (word1, word2)
        combined_value = f"{key[0]}-{key[1]}"
        self._data[key] = combined_value
    def get(self, key: tuple) -> str | None:
        return self._data.get(key)
    def __repr__(self):
        return repr(dict(sorted(self._data.items())))
if __name__ == '__main__':
    d = WordPairDict()
    d.add("Hello", "World")
    d.add("HELLO", "WORLD")
    print(d.get(("hello", "world")))