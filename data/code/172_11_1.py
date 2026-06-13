def match_keys_to_words(input_dict):
    output_dict = {}
    for key, value in input_dict.items():
        output_dict[key] = value
    return output_dict
if __name__ == '__main__':
    sample_data = {
        "apple": "fruit",
        "banana": "fruit",
        "carrot": "vegetable",
        "broccoli": "vegetable",
        "grape": "fruit"
    }
    result = match_keys_to_words(sample_data)
    print(result)