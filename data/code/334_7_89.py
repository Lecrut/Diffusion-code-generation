class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{word1} {word2}"
        if key in self._data:
            return False
        else:
            self._data[key] = value
            return True
    def get(self, word1, word2):
        key = (word1.lower(), word2.lower())
        return self._data.get(key)
if __name__ == '__main__':
    d = WordPairDict()
    result = []
    pairs = [("hello", "world"), ("HELLO", "WORLD"), ("python", "code")]
    for w1, w2 in pairs:
        if d.add(w1, w2):
            result.append(f"Added '{w1}' and '{w2}'")
    print("Dictionary contents:")
    for k, v in sorted(d._data.items()):
        print(f"{k}: {v}")
if __name__ == '__main__':
    d = WordPairDict()
    result = []
    pairs = [("hello", "world"), ("HELLO", "WORLD"), ("python", "code")]
    for w1, w2 in pairs:
        if d.add(w1, w2):
            result.append(f"Added '{w1}' and '{w2}'")
print("Dictionary contents:")
for k, v in sorted(d._data.items()):
    print(f"{k}: {v}")