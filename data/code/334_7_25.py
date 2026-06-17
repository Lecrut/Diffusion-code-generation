class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, pair_tuple, combined_string):
        if not isinstance(pair_tuple, tuple) or len(pair_tuple) != 2:
            raise ValueError("Key must be a tuple of exactly two words.")
        key = (pair_tuple[0], pair_tuple[1])
        self._data[key] = combined_string
    def get(self, pair_tuple):
        if not isinstance(pair_tuple, tuple) or len(pair_tuple) != 2:
            raise ValueError("Key must be a tuple of exactly two words.")
        key = (pair_tuple[0], pair_tuple[1])
        return self._data.get(key)
    def __contains__(self, pair_tuple):
        if not isinstance(pair_tuple, tuple) or len(pair_tuple) != 2:
            raise ValueError("Key must be a tuple of exactly two words.")
        key = (pair_tuple[0], pair_tuple[1])
        return key in self._data
    def __iter__(self):
        for item in self._data.items():
            yield item
if __name__ == '__main__':
    d = WordPairDict()
    d.add(("apple", "pie"), "aplepie")
    d.add(("cat", "dog"), "caddog")
    assert ("apple", "pie") in d and d.get(("apple", "pie")) == "aplepie"
    assert ("cat", "dog") in d and d.get(("cat", "dog")) == "caddog"
    print("All tests passed.")