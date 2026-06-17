class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1.lower(), word2.lower()) if len(word1) > 0 and len(word2) > 0 else (None, None)
        combined = f"{key[0]}-{key[1]}"
        self._data[key] = combined
    def get(self, word1: str, word2: str):
        key = (word1.lower(), word2.lower()) if len(word1) > 0 and len(word2) > 0 else (None, None)
        return self._data.get(key)
if __name__ == '__main__':
    d = WordPairDict()
    d.add("apple", "banana")
    print(d.get("Apple", "Banana"))