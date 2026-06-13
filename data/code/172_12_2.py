class WordMatcher:
    def __init__(self, word_to_key_map):
        self._word_to_key = word_to_key_map
    def match_key_to_word(self, key):
        return self._word_to_key.get(key)
if __name__ == '__main__':
    sample_mapping = {
        "apple": "fruit1",
        "banana": "fruit2",
        "carrot": "vegetable1",
        "broccoli": "vegetable2"
    }
    matcher = WordMatcher(sample_mapping)
    print(f"Matching 'apple': {matcher.match_key_to_word('apple')}")
    print(f"Matching 'banana': {matcher.match_key_to_word('banana')}")
    print(f"Matching 'carrot': {matcher.match_key_to_word('carrot')}")
    print(f"Matching 'grape': {matcher.match_key_to_word('grape')}")