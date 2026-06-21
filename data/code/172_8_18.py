import re

def is_valid_key(key):
    try:
        int(key)
        return True
    except ValueError:
        return False

def is_simple_word(word):
    return isinstance(word, str) and re.match(r'^\w+$', word)

def filter_and_map(dictionary):
    filtered_mapping = {}
    for key, value in dictionary.items():
        if is_valid_key(key) and is_simple_word(value):
            filtered_mapping[int(key)] = value
    return filtered_mapping

if __name__ == '__main__':
    sample_dictionary = {
        "1": "apple",
        "2": "banana",
        "3": "carrot",
        "4": "broccoli",
        "5": "grape"
    }
    result = filter_and_map(sample_dictionary)
    print(result)