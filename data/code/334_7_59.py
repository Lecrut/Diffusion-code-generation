class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        combined = f"{key[0]}-{key[1]}"
        if key in self._data and self._data[key] != combined:
            return False
        else:
            self._data[key] = combined
            return True
    def get(self, word1, word2):
        key = (word1.lower(), word2.lower())
        return self._data.get(key)
if __name__ == '__main__':
    d = WordPairDict()
    assert d.add("Hello", "World") is True
    assert d.get("hello", "world") == "hello-world"
    print(d.get("HELLO", "WORLD"))
    exit(0)