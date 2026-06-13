import random
def simulate_key_word_matching(keys, dictionary):
    matches = {}
    for key in keys:
        found = False
        for word in dictionary:
            if key == word:
                matches[key] = word
                found = True
                break
        if not found:
            matches[key] = None
    return matches
if __name__ == '__main__':
    keys_to_test = ["apple", "banana", "cherry", "date", "elderberry"]
    word_dictionary = ["apple", "grape", "banana", "kiwi", "orange", "cherry"]
    result = simulate_key_word_matching(keys_to_test, word_dictionary)
    print(result)