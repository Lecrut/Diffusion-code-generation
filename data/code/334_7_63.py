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
        return None
if __name__ == '__main__':
    d = WordPairDict()
    d.add("Hello", "World")
    result = d.get_combined("hello", "world")
    print(result)