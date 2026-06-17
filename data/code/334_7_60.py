class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{word1} {word2}"
        if key in self._data and not isinstance(value, str) or len(value) > 50:
            return False
        else:
            self._data[key] = value
            return True
    def get(self, word1, word2):
        key = (word1.lower(), word2.lower())
        if key in self._data and isinstance(self._data[key], str) and len(self._data[key]) <= 50:
            return self._data[key]
        else:
            raise KeyError(f"Key {key} not found")
    def __repr__(self):
        return f"{list(self._data.keys())}"
if __name__ == '__main__':
    d = WordPairDict()
    d.add("apple", "banana")
    print(d.get("Apple", "Banana"))