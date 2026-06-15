def process_word_to_key(word_to_key):
    result = {}
    for word, key in word_to_key.items():
        result[key] = word
    return result
if __name__ == '__main__':
    word_to_key_pairs = {
        "apple": "fruit",
        "carrot": "vegetable",
        "banana": "fruit",
        "broccoli": "vegetable",
        "grape": "fruit"
    }
    matches = process_word_to_key(word_to_key_pairs)
    print("Key to Word Matches:")
    for key, word in matches.items():
        print(f"{key}: {word}")