class DictionaryMapper:
    def __init__(self):
        self.word_to_key = {}
        self.key_to_word = {}
    def build_mapping(self, dictionary):
        for word, key in dictionary.items():
            if word not in self.word_to_key:
                self.word_to_key[word] = key
                self.key_to_word[key] = word
    def get_word_from_key(self, key):
        return self.key_to_word.get(key)
if __name__ == '__main__':
    sample_dictionary = {
        "apple": "fruit",
        "banana": "fruit",
        "carrot": "vegetable",
        "broccoli": "vegetable",
        "grape": "fruit"
    }
    mapper = DictionaryMapper()
    mapper.build_mapping(sample_dictionary)
    print("--- Mapping Results ---")
    print("Word to Key Mapping:")
    for word, key in mapper.word_to_key.items():
        print(f"{word}: {key}")
    print("\nKey to Word Mapping:")
    for key, word in mapper.key_to_word.items():
        print(f"{key}: {word}")
    print("\nLookup Test:")
    print(f"Word 'apple' maps to key: {mapper.word_to_key.get('apple')}")
    print(f"Key 'fruit' maps to word: {mapper.key_to_word.get('fruit')}")