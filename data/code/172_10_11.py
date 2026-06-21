def validate_input(input_dict):
    if not isinstance(input_dict, dict):
        raise ValueError("Input must be a dictionary.")
    for key, value in input_dict.items():
        if not (isinstance(key, int) and isinstance(value, str)):
            raise ValueError("Dictionary keys must be integers and values must be strings.")

def reverse_mapping(word_to_key_map):
    validate_input(word_to_key_map)
    reverse_map = {}
    for word, key in word_to_key_map.items():
        reverse_map[key] = word
    return reverse_map

if __name__ == '__main__':
    sample_data = {
        1: "apple",
        2: "banana",
        3: "carrot",
        4: "grape"
    }
    result = reverse_mapping(sample_data)
    print(result)