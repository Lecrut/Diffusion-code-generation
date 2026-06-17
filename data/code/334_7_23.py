class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word_pair):
        if isinstance(word_pair, tuple) and len(word_pair) == 2:
            key = (word_pair[0], word_pair[1])
            value = f"{word_pair[0]}{word_pair[1]}"
            self._data[key] = value
    def get(self, word_pair):
        if isinstance(word_pair, tuple) and len(word_pair) == 2:
            return self._data.get((word_pair[0], word_pair[1]))
        return None
    def __repr__(self):
        return f"WordPairDict({dict(sorted(self._data.items()))})"
if __name__ == '__main__':
    d = WordPairDict()
    d.add(("apple", "pie"))
    d.add(("cat", "dog"))
    print(d.get(("apple", "pie")))
    assert d.get(("apple", "pie")) == "applepie"
    exit(0)