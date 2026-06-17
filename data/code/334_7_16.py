class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word_pair):
        if isinstance(word_pair, tuple) and len(word_pair) == 2:
            key1, key2 = map(str.lower, word_pair)
            combined_key = f"{key1}_{key2}"
            value = f"{word_pair[0]} {word_pair[1]}"
            self._data[key1] = (combined_key, value)
    def get(self, word):
        if word in self._data:
            return self._data[word][1]
        return None
if __name__ == '__main__':
    d = WordPairDict()
    pairs = [("apple", "banana"), ("cat", "dog")]
    for p in pairs:
        d.add(p)
    print(d.get("apple"))