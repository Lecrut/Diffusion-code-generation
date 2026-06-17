class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1.lower(), word2.lower()) if isinstance(word1, str) and isinstance(word2, str) else (word1, word2)
        combined_value = f"{key[0]} {key[1]}"
        self._data[key] = combined_value
    def get(self, key):
        return self._data.get(key)
if __name__ == '__main__':
    d = WordPairDict()
    d.add("Hello", "World")
    d.add("HELLO", "world")
    print(d.get(("hello", "world")))