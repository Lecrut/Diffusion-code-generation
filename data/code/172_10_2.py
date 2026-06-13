def reverse_mapping(word_to_key):
    reverse = {}
    for key, word in word_to_key.items():
        reverse[key] = word
    return reverse
if __name__ == '__main__':
    sample_data = {
        "apple": "fruit",
        "banana": "fruit",
        "carrot": "vegetable",
        "broccoli": "vegetable",
        "grape": "fruit"
    }
    result = reverse_mapping(sample_data)
    print(result)