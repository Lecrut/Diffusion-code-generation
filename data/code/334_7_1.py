class OptimizedWordDict:
    def __init__(self):
        self._data = {}
    def add(self, word_pair, combined_string):
        if len(word_pair) == 2 and isinstance(combined_string, str):
            key = tuple(sorted((word_pair[0], word_pair[1])))
            self._data[key] = combined_string
        return True
    def get_combined(self, input_word_1, input_word_2):
        if len(input_word_1) == 0 or len(input_word_2) == 0:
            raise ValueError("Input words cannot be empty")
        key_tuple = tuple(sorted((input_word_1, input_word_2)))
        return self._data.get(key_tuple, f"{input_word_1}{input_word_2}")
    def __repr__(self):
        return str(self._data)
def main():
    d = OptimizedWordDict()
    sample_pairs = [
        ("apple", "banana"),
        ("cat", "dog"),
        ("elephant", "fish")
    ]
    combined_samples = {
        ("apple", "banana"): "aplebananabana",
        ("cat", "dog"): "caddog" + "dodog",
        ("elephant", "fish"): "elphishfiseh"
    }
    for i, pair in enumerate(sample_pairs):
        word1 = pair[0]
        word2 = pair[1]
        if (word1, word2) not in combined_samples:
            result = d.get_combined(word1, word2)
        else:
            result = combined_samples[(pair[0], pair[1])]
        print(f"Pair {i+1}: '{word1}', '{word2}' -> Result: {result}")
if __name__ == '__main__':
    main()