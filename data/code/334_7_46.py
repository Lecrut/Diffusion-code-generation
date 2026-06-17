class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1.lower(), word2.lower()) if isinstance(word1, str) and isinstance(word2, str) else (str(word1), str(word2))
        value = f"{key[0]} {key[1]}"
        self._data[key] = value
    def get(self, key: tuple) -> str | None:
        return self._data.get(key) if isinstance(key, tuple) and len(key) == 2 else None
if __name__ == '__main__':
    d = WordPairDict()
    d.add("Hello", "World")
    d.add("HELLO", "WORLD")
    assert d.get(("hello", "world")) == "hello world"
    print(d._data)