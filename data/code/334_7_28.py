class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word_pair):
        key1, key2 = word_pair[0], word_pair[1]
        combined_key = (key1, key2)
        if combined_key in self._data:
            return False
        else:
            value = f"{key1}{key2}"
            self._data[combined_key] = value
            return True
    def get(self, word_pair):
        try:
            return self._data[word_pair]
        except KeyError:
            return None
if __name__ == '__main__':
    d = WordPairDict()
    test_pairs = [("apple", "banana"), ("cat", "dog")]
    for pair in test_pairs:
        result = d.add(pair)
        print(f"Added {pair}: {result}")
    retrieved = d.get(("apple", "banana"))
    if retrieved is not None:
        print(f"Retrieved value: {retrieved}")