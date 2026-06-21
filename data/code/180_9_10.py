def check_word_in_list(target, identifiers):
    if not isinstance(target, str) or not isinstance(identifiers, list):
        raise TypeError("Target must be a string and identifiers must be a list")
    return target in identifiers

if __name__ == '__main__':
    sample_target = "example"
    sample_identifiers = ["apple", "banana", "cherry", "date"]
    print(check_word_in_list(sample_target, sample_identifiers))