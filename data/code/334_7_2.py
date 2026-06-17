class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word_pair_str):
        words = word_pair_str.split()
        key = tuple(words)
        value = ' '.join(words).upper()
        if len(key) == 2 and all(len(w) > 0 for w in key):
            self._data[key] = value
    def get(self, word_pair_str):
        words = word_pair_str.split()
        key = tuple(words)
        return self._data.get(key)
    def __repr__(self):
        return f"WordPairDict({list(self._data.items())})"
if __name__ == '__main__':
    d = WordPairDict()
    d.add("hello world")
    d.add("foo bar")
    print(d.get("hello world"))
    print(repr(d))