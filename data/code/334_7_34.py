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
if __name__ == '__main__':
    d = WordPairDict()
    d.add("hello", "world")
    d.add("foo", "bar")
    print(d.get_combined("hello", "world"))
    print(d.get_combined("foo", "bar"))