class DictionaryMapper:
    def __init__(self):
        self.mapping = {}
    def build_mapping(self, dictionary):
        for key, value in dictionary.items():
            if isinstance(value, str):
                self.mapping[key] = value
            else:
                self.mapping[key] = ""
    def get_word(self, key):
        return self.mapping.get(key, "")
if __name__ == '__main__':
    sample_dictionary = {
        "apple": "fruit",
        "banana": "fruit",
        "carrot": "vegetable",
        "broccoli": "vegetable",
        "water": "liquid"
    }
    mapper = DictionaryMapper()
    mapper.build_mapping(sample_dictionary)
    print(f"Mapping for 'apple': {mapper.get_word('apple')}")
    print(f"Mapping for 'banana': {mapper.get_word('banana')}")
    print(f"Mapping for 'carrot': {mapper.get_word('carrot')}")
    print(f"Mapping for 'broccoli': {mapper.get_word('broccoli')}")
    print(f"Mapping for 'grape': {mapper.get_word('grape')}")