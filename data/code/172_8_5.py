class WordMapper:
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
    mapper = WordMapper()
    mapper.build_mapping(sample_dictionary)
    print("Mapping successful.")
    print("\nTesting retrieval:")
    print("Key 'fruit' maps to word:", mapper.get_word_from_key("fruit"))
    print("Key 'vegetable' maps to word:", mapper.get_word_from_key("vegetable"))
    print("Key 'fruit' maps to word (again):", mapper.get_word_from_key("fruit"))
    print("Key 'unknown' maps to word:", mapper.get_word_from_key("unknown"))