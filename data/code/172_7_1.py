def match_keys_to_words(data):
    mapping = {}
    for key, word in data.items():
        mapping[key] = word
    return mapping
if __name__ == '__main__':
    input_data = {
        "apple": "fruit",
        "carrot": "vegetable",
        "banana": "fruit",
        "broccoli": "vegetable"
    }
    result_mapping = match_keys_to_words(input_data)
    print("Input Data:")
    for key, value in input_data.items():
        print(f"{key}: {value}")
    print("\nSorted Output (Alphabetical by Key):")
    sorted_keys = sorted(result_mapping.keys())
    for key in sorted_keys:
        print(f"{key}: {result_mapping[key]}")