class KeyWordMatcher:
    DEFAULT_KEY = "UNKNOWN"

    @staticmethod
    def create_mapping(words):
        return {word: f"token{index+1}" for index, word in enumerate(words)}

    def __init__(self, words):
        self._mapping = KeyWordMatcher.create_mapping(words)

    def match_key_to_word(self, key):
        return self._mapping.get(key, KeyWordMatcher.DEFAULT_KEY)

if __name__ == '__main__':
    sample_words = ["apple", "banana", "carrot", "broccoli"]
    matcher = KeyWordMatcher(sample_words)
    print(f"Matching 'apple': {matcher.match_key_to_word('apple')}")
    print(f"Matching 'banana': {matcher.match_key_to_word('banana')}")
    print(f"Matching 'carrot': {matcher.match_key_to_word('carrot')}")
    print(f"Matching 'grape': {matcher.match_key_to_word('grape')}")