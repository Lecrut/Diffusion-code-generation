def match_keys_to_words(key_dictionary, dictionary):
    matches = {}
    for key in key_dictionary:
        if key in dictionary:
            matches[key] = dictionary[key]
        else:
            matches[key] = None
    return matches
if __name__ == '__main__':
    key_dict = {
        "apple": "fruit",
        "carrot": "vegetable",
        "banana": "fruit",
        "grape": "fruit"
    }
    word_dict = {
        "apple": "fruit",
        "carrot": "vegetable",
        "banana": "fruit",
        "orange": "citrus"
    }
    result = match_keys_to_words(key_dict, word_dict)
    print(result)