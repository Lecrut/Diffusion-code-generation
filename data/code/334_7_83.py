class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1.lower(), word2.lower())
        combined = f"{key[0]}-{key[1]}"
        if not isinstance(combined, str):
            raise TypeError("Combined string must be a string")
        self._data[key] = combined
    def get(self, word1: str, word2: str) -> str | None:
        key = (word1.lower(), word2.lower())
        return self._data.get(key)
    def __contains__(self, pair):
        if not isinstance(pair, tuple) or len(pair) != 2:
            raise TypeError("Pair must be a tuple of two strings")
        return pair[0].lower() in [k[0] for k in self._data.keys()] and \
               any(k == (pair[0].lower(), pair[1].lower()) or 
                   (k != (pair[0].lower(), pair[1].lower())) for k in self._data.keys())
    def __repr__(self):
        return f"WordPairDict({list(self._data.items())})"
if __name__ == '__main__':
    d = WordPairDict()
    d.add("Hello", "World")
    d.add("HELLO", "WORLD")
    assert d.get("hello", "world") == "hello-world"
    print(d)