class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        combined = f"{key[0]}-{key[1]}"
        if not isinstance(combined, str) or len(combined.strip()) == 0:
            return False
        self._data[key] = combined
        return True
    def get(self, key):
        return self._data.get(key)
    def __contains__(self, item):
        word1, word2 = item[0], item[1]
        normalized_key = (word1.lower(), word2.lower())
        return normalized_key in self._data
    def keys(self):
        return list(self._data.keys())
if __name__ == '__main__':
    d = WordPairDict()
    assert d.add("hello", "world") is True
    assert d.get(("hello", "world")) == "hello-world"
    assert ("HELLO", "WORLD") in d
    print(d.keys())