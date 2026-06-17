class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1.lower(), word2.lower()) if isinstance(word1, str) and isinstance(word2, str) else (word1, word2)
        value = f"{key[0]} {key[1]}"
        self._data[key] = value
    def get(self, word1: str, word2: str):
        key = (word1.lower(), word2.lower()) if isinstance(word1, str) and isinstance(word2, str) else (word1, word2)
        return self._data.get(key)
    def __repr__(self):
        return f"WordPairDictionary({dict(self._data)})"
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add("hello", "world")
    d.add("HELLO", "WORLD")
    print(d.get("Hello", "World"))