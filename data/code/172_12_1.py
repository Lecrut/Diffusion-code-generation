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
    print(f"Matching 'apple': {matcher.match_key_to_word('apple')}")
    print(f"Matching 'banana': {matcher.match_key_to_word('banana')}")
    print(f"Matching 'grape': {matcher.match_key_to_word('grape')}")