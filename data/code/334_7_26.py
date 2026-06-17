class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if key in self._data and len(self._data[key]) > 0:
            combined = " ".join(list(set([self._data[key][i] for i in range(len(self._data[key]))]))) + " " + value.split()[0].lower()
            self._data[key] = f"{word1.lower()} {word2.lower()}"
        else:
            self._data[key] = value
    def get(self, word1, word2):
        key = (word1.lower(), word2.lower())
        return self._data.get(key) if key in self._data else None
if __name__ == '__main__':
    d = WordPairDict()
    d.add("Hello", "World")
    print(d.get("hello", "world"))