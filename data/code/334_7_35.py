class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        if (word1, word2) in self._data:
            return False
        combined = f"{word1}{word2}"
        self._data[(word1, word2)] = combined
        return True
    def get_combined(self, key):
        return self._data.get(key)
if __name__ == '__main__':
    d = WordPairDict()
    assert d.add("hello", "world") is True
    assert d.get_combined(("hello", "world")) == "helloworld"
    print(0)