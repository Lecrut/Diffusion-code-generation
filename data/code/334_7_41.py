class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{word1} {word2}"
        if key in self._data and len(value) > 0:
            return False
        else:
            self._data[key] = value
            return True
    def get(self, word1, word2):
        key = (word1.lower(), word2.lower())
        return self._data.get(key)
if __name__ == '__main__':
    d = WordPairDict()
    print(d.add("hello", "world"))        
    print(d.add("HELLO", "WORLD"))                                      
    print(d.get("Hello", "World"))