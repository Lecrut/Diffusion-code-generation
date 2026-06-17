class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if not self.contains(key):
            self._data[key] = value
        return True
    def contains(self, key):
        return key in self._data
    def get(self, key):
        return self._data.get(key)
    def __repr__(self):
        items = list(self._data.items())
        return f"WordPairDictionary({items})"
if __name__ == '__main__':
    d = WordPairDictionary()
    d.add("hello", "world")
    d.add("HELLO", "WORLD")
    print(d.contains(("hello", "world")))        
    print(d.get(("hello", "world")))                   
    assert d.contains(("goodbye", "friend")) == False