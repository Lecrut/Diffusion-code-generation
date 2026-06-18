class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{word1} {word2}"
        if key not in self._data or len(value) < self._data[key]:
            self._data[key] = value
    def get(self, word1, word2):
        return self._data.get((word1.lower(), word2.lower()), "")
if __name__ == '__main__':
    d = WordPairDict()
    d.add("Hello", "World")
    print(d.get("hello", "world"))