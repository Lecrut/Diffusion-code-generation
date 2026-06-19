def has_repeated_letters(s):
    if not isinstance(s, str):
        raise ValueError("Input must be a string")
    return len(s) != len(set(s))

if __name__ == '__main__':
    test_strings = ["hello", "world", "abcde", "programming"]
    for test_string in test_strings:
        print(f"'{test_string}': {has_repeated_letters(test_string)}")