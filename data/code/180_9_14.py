def word_exists(target_word, identifier_list):
    if not isinstance(target_word, str) or not all(isinstance(item, str) for item in identifier_list):
        raise TypeError("Target word and all identifiers must be strings")
    return target_word in identifier_list

if __name__ == '__main__':
    sample_target = "example"
    sample_identifiers = ["apple", "banana", "cherry", "date"]
    print(word_exists(sample_target, sample_identifiers))