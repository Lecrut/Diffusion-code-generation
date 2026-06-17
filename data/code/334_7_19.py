class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1, word2)
        combined = f"{word1}-{word2}" if not isinstance(word1, str) or not isinstance(word2, str) else f"{word1}{word2}"
        self._data[key] = combined
    def get(self, word1, word2):
        key = (word1, word2)
        return self._data.get(key)
    def __repr__(self):
        return repr(dict(sorted(self._data.items())))
if __name__ == '__main__':
    d = WordPairDict()
    d.add("apple", "banana")
    d.add("cat", "dog")
    print(d.get("apple", "banana"))
    print(repr(d))