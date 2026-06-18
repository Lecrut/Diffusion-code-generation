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
        if key not in self._data:
            raise KeyError(f"Pair ({word1}, {word2}) not found")
        return self._data[key]
if __name__ == '__main__':
    d = WordPairDict()
    test_pairs = [
        ("apple", "banana"),
        ("cat", "dog"),
        ("elephant", "frog")
    ]
    for w1, w2 in test_pairs:
        result = d.add(w1, w2)
    assert d.get_combined("apple", "banana") == "applebanana"
    assert d.get_combined("cat", "dog") == "catdog"
    for key, value in d._data.items():
        print(f"{key} -> {value}")
print("Execution successful.")