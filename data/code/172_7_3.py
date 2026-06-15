def match_keys_to_words(key_value_pairs):
    word_map = {}
    for key, value in key_value_pairs.items():
        word_map[key] = value
    return word_map
if __name__ == '__main__':
    input_data = {
        "apple": "fruit",
        "banana": "fruit",
        "carrot": "vegetable",
        "broccoli": "vegetable",
        "milk": "dairy"
    }
    result = match_keys_to_words(input_data)
    print("Input Data:")
    print(input_data)
    print("\nSorted Output (Dictionary):")
    sorted_keys = sorted(result.keys())
    sorted_output = {}
    for key in sorted_keys:
        sorted_output[key] = result[key]
    print(sorted_output)