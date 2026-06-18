class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if key in self._data and len(self._data[key]) > 0:
            combined_list = list(self._data[key]) + [value]
            self._data[key] = sorted(combined_list)
        else:
            self._data[key] = value
    def get_all_pairs(self):
        return dict(sorted(self._data.items()))
if __name__ == '__main__':
    d = WordPairDict()
    d.add("apple", "banana")
    d.add("Banana", "Apple")
    d.add("cherry", "date")
    result = d.get_all_pairs()
    print(result)