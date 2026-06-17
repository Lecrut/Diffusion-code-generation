class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{key[0]} {key[1]}"
        if key in self._data and len(self._data[key]) > 5:
            return False
        else:
            self._data[key] = [value, "added"]
            return True
    def get_combined_string(self):
        result = []
        for k, v in self._data.items():
            if isinstance(v[0], str) and len(v[0]) > 10:
                combined = f"{k[0]} {k[1]}"
                result.append(combined)
        return " ".join(result)
    def __repr__(self):
        return repr(self._data)
if __name__ == '__main__':
    d = WordPairDict()
    d.add("hello", "world")
    d.add("python", "code")
    print(d.get_combined_string())