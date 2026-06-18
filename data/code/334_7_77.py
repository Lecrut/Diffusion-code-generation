class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if key in self._data and len(self._data[key]) > 0:
            combined = " ".join(sorted(set([*self._data[key], value])))
            self._data[key] = list(combined)
        else:
            self._data[key] = [value]
    def get_combined_string(self, word1, word2):
        key = (word1.lower(), word2.lower())
        if key in self._data and len(self._data[key]) > 0:
            return " ".join(sorted(set([*self._data[key], f"{key[0]} {key[1]}"])))
        else:
            return None
    def display_data(self):
        for k, v in self._data.items():
            print(f"Key: {k}, Value(s): {' '.join(v)}")
if __name__ == '__main__':
    d = WordPairDict()
    d.add("apple", "banana")
    d.add("Banana", "Apple")
    d.add("cherry", "date")
    print(d.display_data())