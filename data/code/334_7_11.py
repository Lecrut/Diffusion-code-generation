class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if key in self._data and self._data[key] != value:
            return False
        else:
            self._data[key] = value
            return True
    def get(self, word1, word2):
        key = (word1.lower(), word2.lower())
        return self._data.get(key)
    def __repr__(self):
        return f"WordPairDictionary({list(self._data.items())})"
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add("Hello", "World")
    d.add("HELLO", "WORLD")
    print(d.get("hello", "world"))