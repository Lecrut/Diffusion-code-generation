class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}" if len(key) == 2 else ""
        self._data[key] = value
    def get(self, word1: str, word2: str):
        return self._data.get((word1.lower(), word2.lower()))
if __name__ == '__main__':
    d = WordPairDict()
    d.add("hello", "world")
    result = d.get("HELLO", "WORLD")
    print(result)