def process_word_to_key(word_to_key_pairs):
    key_to_word_matches = {}
    for word, key in word_to_key_pairs.items():
        key_to_word_matches[key] = word
    return key_to_word_matches
if __name__ == '__main__':
    word_to_key_config = {
        "apple": "A1",
        "banana": "B2",
        "cherry": "C3",
        "date": "D4"
    }
    results = process_word_to_key(word_to_key_config)
    print("Key to Word Matches:")
    for key, word in results.items():
        print(f"{key}: {word}")