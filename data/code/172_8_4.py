import collections
def build_word_map(dictionary):
    word_map = {}
    for key, value in dictionary.items():
        if isinstance(value, str):
            word_map[key] = value
    return word_map
if __name__ == '__main__':
    sample_dictionary = {
        "apple": "fruit",
        "banana": "fruit",
        "carrot": "vegetable",
        "broccoli": "vegetable",
        "milk": "dairy",
        "cheese": "dairy",
        "water": "liquid"
    }
    word_mapping = build_word_map(sample_dictionary)
    print(word_mapping)