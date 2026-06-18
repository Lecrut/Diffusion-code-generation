class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if key in self._data and not self._data[key].endswith(value.split()[-1]):
            return False
        else:
            self._data[key] = value
            return True
    def get(self, word1, word2):
        key = (word1.lower(), word2.lower())
        if key in self._data:
            return self._data[key]
        return None
    def __repr__(self):
        return str(self._data)
if __name__ == '__main__':
    d = WordPairDict()
    d.add("hello", "world")
    d.add("HELLO", "WORLD")
    print(d.get("Hello", "World"))