import collections
def build_word_map(dictionary):
    word_map = {}
    for key, word in dictionary.items():
        word_map[key] = word
    return word_map
if __name__ == '__main__':
    sample_dictionary = {
        "apple": "fruit",
        "carrot": "vegetable",
        "banana": "fruit",
        "broccoli": "vegetable",
        "grape": "fruit"
    }
    word_mapping = build_word_map(sample_dictionary)
    print(word_mapping)