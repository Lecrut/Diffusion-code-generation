class WordMatcher:
    def __init__(self, word_to_key_mapping):
        self._mapping = word_to_key_mapping
    def match_key_to_word(self, key):
        return self._mapping.get(key)
if __name__ == '__main__':
    sample_mapping = {
        "apple": "A1",
        "banana": "B2",
        "cherry": "C3",
        "date": "D4"
    }
    matcher = WordMatcher(sample_mapping)
    key1 = "apple"
    result1 = matcher.match_key_to_word(key1)
    print(f"Key: {key1}, Word: {result1}")
    key2 = "cherry"
    result2 = matcher.match_key_to_word(key2)
    print(f"Key: {key2}, Word: {result2}")
    key3 = "grape"
    result3 = matcher.match_key_to_word(key3)
    print(f"Key: {key3}, Word: {result3}")