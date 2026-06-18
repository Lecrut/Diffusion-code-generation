class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{word1} {word2}"
        if not isinstance(key, tuple) or len(key) != 2:
            raise ValueError("Key must be a pair of two words")
        self._data[key] = value
    def get(self, key):
        return self._data.get(key)
    def __contains__(self, key):
        if isinstance(key, tuple) and len(key) == 2:
            return key in self._data
        return False
    def keys(self):
        return list(self._data.keys())
if __name__ == '__main__':
    d = WordPairDict()
    d.add("hello", "world")
    d.add("HELLO", "WORLD")
    assert (d.get(("hello", "world")) or "").strip().lower() == f"{('hello', 'world')[0]} {('hello', 'world')[1]}"
    print(0)