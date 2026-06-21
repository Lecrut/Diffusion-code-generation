def word_exists(target_word, identifier_list):
    if not isinstance(target_word, str) or not isinstance(identifier_list, list):
        raise TypeError("Target word must be a string and identifiers must be a list")
    return target_word in identifier_list

if __name__ == '__main__':
    sample_target = "example"
    sample_identifiers = ["apple", "banana", "cherry", "date"]
    print(word_exists(sample_target, sample_identifiers))