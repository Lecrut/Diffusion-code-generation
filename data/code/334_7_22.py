class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add_pair(self, word1, word2):
        key = (word1, word2)
        if key in self._data:
            return False
        value = f"{word1}-{word2}"
        self._data[key] = value
        return True
    def get_combined_string(self, word1, word2):
        key = (word1, word2)
        if key not in self._data:
            raise KeyError(f"Pair ({word1}, {word2}) not found")
        return self._data[key]
if __name__ == '__main__':
    d = WordPairDictionary()
    test_cases = [
        ("apple", "banana"),
        ("cat", "dog"),
        ("elephant", "frog"),
    ]
    for w1, w2 in test_cases:
        if not d.add_pair(w1, w2):
            print(f"Warning: Pair ({w1}, {w2}) already exists")
    results = []
    for w1, w2 in test_cases:
        try:
            res = d.get_combined_string(w1, w2)
            results.append(res)
        except KeyError as e:
            print(e)
    assert len(results) == 3 and "apple-banana" in results and "cat-dog" in results and "elephant-frog" in results
    exit(0)