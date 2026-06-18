class WordPairDictionary:
    def __init__(self):
        self.data = {}
    def add(self, word_pair, combined_string):
        if isinstance(word_pair, tuple) and len(word_pair) == 2:
            key = f"{word_pair[0]}:{word_pair[1]}"
            self.data[key] = combined_string
        else:
            raise TypeError("Key must be a pair of words.")
    def get(self, word_pair):
        if isinstance(word_pair, tuple) and len(word_pair) == 2:
            key = f"{word_pair[0]}:{word_pair[1]}"
            return self.data.get(key)
        else:
            raise ValueError("Key must be a pair of words.")
    def contains(self, word_pair):
        if isinstance(word_pair, tuple) and len(word_pair) == 2:
            key = f"{word_pair[0]}:{word_pair[1]}"
            return key in self.data
        else:
            raise ValueError("Key must be a pair of words.")
    def __repr__(self):
        return repr(self.data)
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add(("apple", "banana"), "appleanabana")
    d.add(("cat", "dog"), "catdog")
    assert d.contains(("apple", "banana"))
    assert not d.contains(("zebra", "monkey"))
    retrieved = d.get(("cat", "dog"))
    assert retrieved == "catdog"
    print("All tests passed successfully.")