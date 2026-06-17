class WordPairDictionary:
    def __init__(self):
        self._data = {}
    def add(self, word_pair_str):
        words = word_pair_str.split()
        if len(words) != 2:
            raise ValueError("Input must contain exactly two words.")
        key = tuple(sorted([words[0], words[1]]))
        value = " ".join(words)
        self._data[key] = value
    def get(self, word_pair_str):
        try:
            return self._data[tuple(sorted(word_pair_str.split()))]
        except KeyError:
            raise ValueError(f"Key '{word_pair_str}' not found.")
if __name__ == '__main__':
    d = WordPairDictionary()
    sample_inputs = [
        "apple banana",
        "cherry date",
        "elderberry fig",
        "grape honeydew"
    ]
    for inp in sample_inputs:
        d.add(inp)
    print("Stored data:")
    for k, v in sorted(d._data.items()):
        print(f"{k} -> {v}")
    test_query = "banana apple"
    try:
        result = d.get(test_query)
        print(f"\nQuery '{test_query}' returned: {result}")
    except ValueError as e:
        print(f"\nError retrieving query '{test_query}': {e}")