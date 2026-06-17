class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        combined = f"{key[0]}-{key[1]}"
        if key in self._data:
            return False
        else:
            self._data[key] = combined
            return True
    def get(self, word1, word2):
        key = (word1.lower(), word2.lower())
        return self._data.get(key)
if __name__ == '__main__':
    d = WordPairDict()
    result = []
    pairs = [("apple", "banana"), ("Banana", "Apple"), ("cherry", "date")]
    for w1, w2 in pairs:
        if not d.add(w1, w2):
            print(f"Duplicate entry detected for {w1} and {w2}")
        else:
            combined = d.get(w1, w2)
            result.append(combined)
    print(result)