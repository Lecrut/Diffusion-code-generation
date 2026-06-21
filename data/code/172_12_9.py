class KeyValueMatcher:
    WORD_TO_KEY_MAPPING = {
        "apple": "fruit1",
        "banana": "fruit2",
        "carrot": "vegetable1",
        "broccoli": "vegetable2"
    }

    @staticmethod
    def match_key_to_word(key):
        return KeyValueMatcher.WORD_TO_KEY_MAPPING.get(key, "Unknown")

if __name__ == '__main__':
    print(f"Matching 'apple': {KeyValueMatcher.match_key_to_word('apple')}")
    print(f"Matching 'banana': {KeyValueMatcher.match_key_to_word('banana')}")
    print(f"Matching 'carrot': {KeyValueMatcher.match_key_to_word('carrot')}")
    print(f"Matching 'grape': {KeyValueMatcher.match_key_to_word('grape')}")