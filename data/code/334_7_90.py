class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word_pair):
        if len(word_pair) != 2:
            raise ValueError("Key must be a pair of words")
        key = tuple(sorted(word_pair))
        value = " ".join(key)
        self._data[key] = value
    def get(self, word_pair):
        return self._data.get(tuple(sorted(word_pair)))
    def __contains__(self, item):
        return tuple(sorted(item)) in self._data.keys()
    def __len__(self):
        return len(self._data)
    def keys(self):
        return list(self._data.keys())
    def values(self):
        return list(self._data.values())
if __name__ == '__main__':
    d = WordPairDict()
    d.add(["apple", "banana"])
    d.add(["cherry", "date"])
    assert ("apple", "banana") in d
    assert len(d) == 2
    print("All tests passed successfully.")