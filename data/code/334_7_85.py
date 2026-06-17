class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1: str, word2: str) -> None:
        key = (word1.lower(), word2.lower())
        combined = f"{key[0]}-{key[1]}"
        if not isinstance(key, tuple) or len(key) != 2:
            raise ValueError("Key must be a pair of strings")
    def get(self, word1: str, word2: str) -> str | None:
        key = (word1.lower(), word2.lower())
        return self._data.get(key) if isinstance(key, tuple) and len(key) == 2 else None
    def __contains__(self, pair):
        try:
            _ = list(pair)
            return True
        except TypeError:
            return False
    def keys(self):
        return [list(k) for k in self._data.keys()]
if __name__ == '__main__':
    d = WordPairDict()
    d.add("hello", "world")
    print(d.get("HELLO", "WORLD"))