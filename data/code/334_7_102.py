class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        if (word1, word2) in self._data:
            return False
        combined = f"{word1}{word2}"
        self._data[(word1, word2)] = combined
        return True
    def get_combined(self, word_pair):
        key = tuple(word_pair) if isinstance(word_pair, list) else (word_pair[0], word_pair[1])
        return self._data.get(key)
if __name__ == '__main__':
    d = WordPairDict()
    test_pairs = [["apple", "pie"], ["banana", "split"], ("cherry", "tart")]
    for pair in test_pairs:
        result = d.add(*pair) if isinstance(pair, list) else d.add(pair[0], pair[1])
        print(f"Added {pair}, Success={result}")
    lookup_tests = [("apple", "pie"), ["banana", "split"], ("cherry", "tart")]
    for test in lookup_tests:
        key_val = tuple(test) if isinstance(test, list) else (test[0], test[1])
        combined = d.get_combined(key_val)
        print(f"Key {key_val} -> Value '{combined}'")