class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word_pair_str):
        key_tuple = tuple(word_pair_str.split())
        if len(key_tuple) != 2:
            raise ValueError("Key must be a pair of two words")
        combined_string = " ".join(key_tuple)
        self._data[key_tuple] = combined_string
    def get(self, word1, word2):
        key_tuple = (word1, word2)
        return self._data.get(key_tuple, None)
    def __repr__(self):
        items_str = ", ".join(f"{k!r}: {v}" for k, v in sorted(self._data.items()))
        return f"WordPairDict({items_str})"
if __name__ == '__main__':
    d = WordPairDict()
    d.add("apple banana")
    d.add("cat dog")
    result1 = d.get("apple", "banana")
    result2 = d.get("dog", "cat")
    assert result1 is not None and result1 == "apple banana"
    assert result2 is None
    print(d)