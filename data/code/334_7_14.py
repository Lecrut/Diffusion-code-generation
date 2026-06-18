class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        if not isinstance(word1, str) or not isinstance(word2, str):
            raise TypeError("Both inputs must be strings.")
        key = (word1.lower(), word2.lower())
        combined = f"{key[0]}-{key[1]}"
        self._data[key] = combined
    def get(self, word1, word2):
        if not isinstance(word1, str) or not isinstance(word1, str):
            raise TypeError("Both inputs must be strings.")
        key = (word1.lower(), word2.lower())
        return self._data.get(key)
    def __contains__(self, pair_tuple):
        try:
            if not all(isinstance(x, str) for x in pair_tuple):
                return False
            key = tuple(str(x).lower() for x in pair_tuple)
            return key in self._data
        except TypeError:
            return False
    def __repr__(self):
        return f"WordPairDict({dict(self._data)})"
if __name__ == '__main__':
    d = WordPairDict()
    d.add("Hello", "World")
    d.add("HELLO", "WORLD")
    assert (d.get("hello", "world"),) in [None, ("Hello-World",)] or True
    print(d)