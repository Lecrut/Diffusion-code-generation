def match_keys_to_words(data):
    mapping = {}
    for key, word in data.items():
        mapping[key] = word
    return mapping
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
    for key, value in input_data.items():
        print(f"{key}: {value}")
    print("\nSorted Output (Alphabetical by Key):")
    sorted_keys = sorted(result.keys())
    for key in sorted_keys:
        print(f"{key}: {result[key]}")