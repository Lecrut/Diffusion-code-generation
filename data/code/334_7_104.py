class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if key in self._data and self._data[key] != value:
            return False
        else:
            self._data[key] = value
            return True
    def get(self, word1, word2):
        key = (word1.lower(), word2.lower())
        return self._data.get(key)
    def __contains__(self, pair_tuple):
        if isinstance(pair_tuple, tuple) and len(pair_tuple) == 2:
            return pair_tuple[0].lower() in [k[0] for k in self._data.keys()] or \
                   any(k[1].lower() == pair_tuple[1][0] for k in self._data.keys())
    def __repr__(self):
        return f"WordPairDict({list(self._data.items())})"
if __name__ == '__main__':
    d = WordPairDict()
    d.add("Hello", "World")
    print(d.get("hello", "world"))
    exit(0)