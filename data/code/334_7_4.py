class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word_pair_key, combined_value):
        if isinstance(word_pair_key, tuple) and len(word_pair_key) == 2:
            key_str = f"{word_pair_key[0]}-{word_pair_key[1]}"
            self._data[key_str] = combined_value
        else:
            raise ValueError("Key must be a pair of words.")
    def get(self, word_pair_key):
        if isinstance(word_pair_key, tuple) and len(word_pair_key) == 2:
            key_str = f"{word_pair_key[0]}-{word_pair_key[1]}"
            return self._data.get(key_str)
        else:
            raise ValueError("Key must be a pair of words.")
    def __repr__(self):
        items = [f"'{k}': '{v}'" for k, v in sorted(self._data.items())]
        return f"{type(self).__name__}({', '.join(items)})"
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add(("apple", "pie"), "aple-pie")
    d.add(("cat", "dog"), "cat-dog")
    print(d)