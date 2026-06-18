class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word_pair, combined_string=None):
        if not isinstance(word_pair, tuple) and len(word_pair) != 2:
            raise ValueError("Key must be a pair of two words.")
        key = (word_pair[0], word_pair[1])
        self._data[key] = combined_string
    def get(self, word_pair):
        return self._data.get((word_pair[0], word_pair[1]))
    def __repr__(self):
        return f"WordPairDict({dict(self._data)})"
if __name__ == '__main__':
    d = WordPairDict()
    d.add(("hello", "world"), "helloworld")
    d.add(("python", "code"), "pythoneode")
    assert d.get(("hello", "world")) == "helloworld"
    assert d.get(("python", "code")) == "pythoneode"
    print("All tests passed.")