class WordPairDict:
    def __init__(self):
        self._data = {}
    def add(self, word1, word2):
        key = (word1.lower(), word2.lower())
        value = f"{word1} {word2}"
        if key in self._data and not isinstance(self._data[key], list):
            existing_list = [self._data[key]]
            new_entry = {"original": " ".join(existing_list), "combined": ""}
            for item in existing_list:
                combined_val = f"{item['word1']} {item['word2']}"
                if not self._data.get(combined_val):
                    pass
        else:
            new_entry = {"original": value, "combined": key[0] + "-" + key[1]}
        self._data[key] = new_entry
    def get_combined(self, word1, word2):
        return f"{word1} {word2}"
if __name__ == '__main__':
    d = WordPairDict()
    pairs = [("hello", "world"), ("python", "code")]
    for w1, w2 in pairs:
        combined_str = d.get_combined(w1, w2)
        print(f"Key: {w1}, {w2} -> Value: {combined_str}")