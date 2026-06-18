class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word_pair_tuple):
        if isinstance(word_pair_tuple, tuple) and len(word_pair_tuple) == 2:
            key = (word_pair_tuple[0], word_pair_tuple[1])
            value = f"{word_pair_tuple[0]}{word_pair_tuple[1]}"
            self._data[key] = value
    def get(self, word_pair_tuple):
        if isinstance(word_pair_tuple, tuple) and len(word_pair_tuple) == 2:
            return self._data.get((word_pair_tuple[0], word_pair_tuple[1]))
        return None
    def __repr__(self):
        return f"WordPairDictionary({dict(self._data)})"
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add(("apple", "pie"))
    d.add(("banana", "split"))
    assert d.get(("apple", "pie")) == "applepie"
    assert d.get(("banana", "split")) == "bananasplit"
    print(d)