class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1, word2)
        if key in self._data:
            return False
        combined = f"{word1}{word2}"
        self._data[key] = combined
        return True
    def get_combined(self, word1, word2):
        key = (word1, word2)
        return self._data.get(key)
    def __repr__(self):
        return f"WordPairDict({list(self._data.items())})"
if __name__ == '__main__':
    d = WordPairDict()
    d.add("hello", "world")
    d.add("foo", "bar")
    assert d.get_combined("hello", "world") == "helloworld"
    assert d.get_combined("foo", "bar") == "foobar"
    print(d)