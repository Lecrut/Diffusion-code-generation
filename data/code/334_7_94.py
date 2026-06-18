class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        if (word1, word2) in self._data:
            return
        combined = f"{word1}{word2}"
        self._data[(word1, word2)] = combined
    def get_combined(self, key):
        return self._data.get(key, "")
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add("hello", "world")
    d.add("foo", "bar")
    assert d.get_combined(("hello", "world")) == "helloworld"
    assert d.get_combined(("foo", "bar")) == "foobar"
    print(d._data)