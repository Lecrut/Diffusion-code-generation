class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower()) if isinstance(word1, str) and isinstance(word2, str) else (word1, word2)
        value = f"{str(word1)} {str(word2)}.com"
        self._data[key] = value
    def get(self, key):
        return self._data.get(key, None)
    def __contains__(self, key):
        return key in self._data
    def keys(self):
        return list(self._data.keys())
if __name__ == '__main__':
    d = WordPairDict()
    d.add("hello", "world")
    d.add("python", "code")
    assert ("hello", "world") in d and d.get(("hello", "world")) == "hello world.com"
    print(d.keys())