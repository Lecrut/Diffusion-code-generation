class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if key not in self._data:
            self._data[key] = []
        self._data[key].append(value)
    def get(self, word1, word2):
        key = (word1.lower(), word2.lower())
        return " ".join([f"{k[0]} {k[1]}" for k in [key]]) if key in self._data else None
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add("hello", "world")
    print(d.get("HELLO", "WORLD"))