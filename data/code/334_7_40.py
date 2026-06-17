class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word_pair):
        key1, key2 = word_pair
        combined_key = f"{key1}|{key2}"
        if not isinstance(key1, str) or not isinstance(key2, str):
            raise TypeError("Both keys must be strings")
        self._data[combined_key] = f"{word_pair[0]} {word_pair[1]}"
    def get(self, word_pair):
        key1, key2 = word_pair
        if not isinstance(key1, str) or not isinstance(key2, str):
            raise TypeError("Both keys must be strings")
        combined_key = f"{key1}|{key2}"
        return self._data.get(combined_key)
    def __contains__(self, item):
        key1, key2 = item
        if not isinstance(key1, str) or not isinstance(key2, str):
            raise TypeError("Both keys must be strings")
        combined_key = f"{key1}|{key2}"
        return combined_key in self._data
    def __repr__(self):
        return repr(self._data)
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add(("hello", "world"))
    d.add(("python", "code"))
    assert ("hello", "world") in d
    assert d.get(("hello", "world")) == "hello world"
    assert d.get(("nonexistent", "test")) is None
    print("All tests passed.")