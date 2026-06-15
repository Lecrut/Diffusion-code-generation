class WordMapper:
    def __init__(self):
        self.word_to_key = {}
        self.key_to_word = {}
    def build_mapping(self, dictionary):
        for word, key in dictionary.items():
            if word not in self.word_to_key:
                self.word_to_key[word] = key
                self.key_to_word[key] = word
            elif self.word_to_key[word] != key:
                raise ValueError(f"Conflict found for word '{word}'")
    def get_word(self, key):
        return self.key_to_word.get(key)
if __name__ == '__main__':
    sample_dictionary = {
        "apple": "A1",
        "banana": "B2",
        "cherry": "C3",
        "date": "D4",
        "elderberry": "E5"
    }
    mapper = WordMapper()
    mapper.build_mapping(sample_dictionary)
    print("--- Mapping Results ---")
    print("Word to Key Mapping:")
    for word, key in mapper.word_to_key.items():
        print(f"{word}: {key}")
    print("\nKey to Word Mapping (Reverse Lookup):")
    for key, word in mapper.key_to_word.items():
        print(f"{key}: {word}")
    print("\nLookup Test:")
    print(f"Key 'A1' maps to: {mapper.get_word('A1')}")
    print(f"Key 'B2' maps to: {mapper.get_word('B2')}")
    print(f"Key 'D4' maps to: {mapper.get_word('D4')}")
    print(f"Key 'Z9' maps to: {mapper.get_word('Z9')}")