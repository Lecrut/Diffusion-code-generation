class KeyWordMatcher:
    def __init__(self, key_to_word_mapping):
        if not isinstance(key_to_word_mapping, dict) or not all(isinstance(k, int) and isinstance(v, str) for k, v in key_to_word_mapping.items()):
            raise ValueError("Invalid input. Expected a dictionary where keys are integers and values are strings.")
        self._mapping = key_to_word_mapping

    def match_key_to_word(self, key):
        if not isinstance(key, int):
            raise TypeError("Invalid input. Key must be an integer.")
        return self._mapping.get(key, None)

if __name__ == '__main__':
    sample_mapping = {
        1: "apple",
        2: "banana",
        3: "carrot",
        4: "broccoli"
    }
    matcher = KeyWordMatcher(sample_mapping)
    print(f"Matching key 1: {matcher.match_key_to_word(1)}")
    print(f"Matching key 2: {matcher.match_key_to_word(2)}")
    print(f"Matching key 3: {matcher.match_key_to_word(3)}")
    print(f"Matching key 5 (not found): {matcher.match_key_to_word(5)}")