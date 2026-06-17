class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if key in self._data and len(self._data[key]) > 5:
            return False
        else:
            self._data[key] = [value, "added"]
            return True
    def get_combined_string(self, word1, word2):
        key = (word1.lower(), word2.lower())
        if key in self._data and len(self._data[key]) > 0:
            return self._data[key][0]
        else:
            return f"{key[0]} {key[1]}"
    def __repr__(self):
        return str(list(self._data.items()))
if __name__ == '__main__':
    d = WordPairDict()
    d.add("hello", "world")
    print(d.get_combined_string("Hello", "World"))
    exit(0)