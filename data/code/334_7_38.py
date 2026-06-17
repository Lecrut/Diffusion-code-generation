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
            self._data[key] = [value]
    def get_combined_string(self, word1, word2):
        key = (word1.lower(), word2.lower())
        if key in self._data and len(self._data[key]) > 0:
            return " ".join(sorted(set("".join(self._data[key]).split())))
        else:
            raise KeyError(f"Pair ({word1}, {word2}) not found")
    def __repr__(self):
        items = ", ".join([f"{k[0]}:{v}" for k, v in self._data.items()])
        return f"WordPairDict({items})"
if __name__ == '__main__':
    d = WordPairDict()
    d.add("apple", "banana")
    d.add("Banana", "Apple")
    try:
        result = d.get_combined_string("APPLE", "BANANA")
        print(result)
    except KeyError as e:
        print(e)