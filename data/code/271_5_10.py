def contains_only_digits_and_spaces(input_string):
    ALLOWED_CHARS = "0123456789 "
    for char in input_string:
        if char not in ALLOWED_CHARS:
            return False
    return True

if __name__ == '__main__':
    test_strings = ["123 456", "abc 123", "1234abcd", "1234"]
    results = {test_string: contains_only_digits_and_spaces(test_string) for test_string in test_strings}
    print(results)