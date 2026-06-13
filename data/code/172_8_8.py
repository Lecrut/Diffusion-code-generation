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
    print("Word to Key Mapping (for lookup):")
    print(mapper.word_to_key)
    print("\nKey to Word Mapping (for retrieval):")
    print(mapper.key_to_word)
    print("\nRetrieval Tests:")
    print("Word 'apple' maps to key:", mapper.word_to_key.get("apple"))
    print("Word 'carrot' maps to key:", mapper.word_to_key.get("carrot"))
    print("Key 'fruit' maps to word:", mapper.key_to_word.get("fruit"))
    print("Key 'vegetable' maps to word:", mapper.key_to_word.get("vegetable"))
    print("Key 'orange' (non-existent) maps to word:", mapper.key_to_word.get("orange"))