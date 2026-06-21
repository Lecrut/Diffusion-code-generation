def is_valid_key(key):
    return isinstance(key, int)

def is_simple_word(word):
    return word.isalpha()

def filter_and_map(dictionary):
    filtered_dict = {key: value for key, value in dictionary.items() if is_valid_key(key) and is_simple_word(value)}
    return filtered_dict

if __name__ == '__main__':
    sample_dictionary = {
        1: "apple",
        2: "banana",
        3: "carrot",
        4: "broccoli",
        5: "grape"
    }
    result = filter_and_map(sample_dictionary)
    print(result)