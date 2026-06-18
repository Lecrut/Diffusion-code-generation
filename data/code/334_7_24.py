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
    def __contains__(self, pair_tuple):
        if isinstance(pair_tuple, tuple) and len(pair_tuple) == 2:
            return pair_tuple in self._data.keys()
        else:
            raise TypeError("Pair must be a tuple of two strings")
if __name__ == '__main__':
    d = WordPairDict()
    result1 = d.add('apple', 'banana')
    result2 = d.get('Apple', 'Banana')
    print(result1)
    print(result2)