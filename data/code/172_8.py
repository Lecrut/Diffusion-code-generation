class DictionaryMapper:
    def __init__(self):
        self.word_to_key = {}
        self.key_to_word = {}
    def build_mapping(self, dictionary):
        for word, key in dictionary.items():
            if word not in self.word_to_key:
                self.word_to_key[word] = key
                self.key_to_word[key] = word
    def get_word(self, key):
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
    print(f"Word to Key Mapping: {mapper.word_to_key}")
    print(f"Key to Word Mapping: {mapper.key_to_word}")
    print(f"Result for key 'fruit': {mapper.get_word('fruit')}")
    print(f"Result for key 'vegetable': {mapper.get_word('vegetable')}")
    print(f"Result for key 'fruit' (check): {mapper.get_word('fruit')}")