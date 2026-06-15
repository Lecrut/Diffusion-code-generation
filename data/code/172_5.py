def simulate_key_word_matching(keys, dictionary):
    matches = {}
    for key in keys:
        if key in dictionary:
            matches[key] = dictionary[key]
        else:
            matches[key] = None
    return matches
if __name__ == '__main__':
    keys_to_test = ["apple", "banana", "cherry", "date", "elderberry"]
    word_dictionary = {
        "apple": "fruit",
        "banana": "fruit",
        "cherry": "fruit",
        "grape": "fruit",
        "date": "fruit",
        "elderberry": "berry"
    }
    results = simulate_key_word_matching(keys_to_test, word_dictionary)
    print(results)