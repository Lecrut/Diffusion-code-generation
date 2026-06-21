def keys_to_words(keys):
    mapping = {
        "apple": "fruit",
        "banana": "fruit",
        "carrot": "vegetable",
        "broccoli": "vegetable",
        "milk": "dairy"
    }
    return {key: mapping.get(key, 'unknown') for key in keys}

if __name__ == '__main__':
    sample_data = ["apple", "banana", "carrot", "broccoli", "milk", "grape"]
    result = keys_to_words(sample_data)
    print(result)