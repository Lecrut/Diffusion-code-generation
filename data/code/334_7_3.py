class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower()) if isinstance(word1, str) and isinstance(word2, str) else (word1, word2)
        value = f"{key[0]}-{key[1]}"
        self._data[key] = value
    def get(self, word1, word2):
        key = (word1.lower(), word2.lower()) if isinstance(word1, str) and isinstance(word2, str) else (word1, word2)
        return self._data.get(key)
if __name__ == '__main__':
    d = WordPairDict()
    d.add("apple", "banana")
    print(d.get("Apple", "Banana"))