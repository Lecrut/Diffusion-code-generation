class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        if key in self._data:
            return False
        combined = f"{word1} {word2}"
        self._data[key] = combined
        return True
    def get_combined(self, word1, word2):
        key = (word1.lower(), word2.lower())
        if key in self._data:
            return self._data[key]
        raise KeyError(f"Pair ({word1}, {word2}) not found")
if __name__ == '__main__':
    d = WordPairDict()
    d.add("apple", "banana")
    d.add("cat", "dog")
    print(d.get_combined("Apple", "Banana"))
    print(d.get_combined("Cat", "Dog"))