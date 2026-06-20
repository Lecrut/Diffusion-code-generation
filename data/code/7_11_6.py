def has_no_special_chars(s):
    for char in s:
        if not char.isalnum():
            return False
    return True

if __name__ == '__main__':
    sample_strings = ["HelloWorld", "Test123", "Invalid@Char", "NoSpecialsHere", "12345"]
    for test_str in sample_strings:
        result = has_no_special_chars(test_str)
        print(f"{test_str}: {result}")