def has_special_chars(s):
    for char in s:
        if not char.isalnum() and not char.isspace():
            return True
    return False

if __name__ == '__main__':
    test_cases = [
        "HelloWorld",
        "Hello World",
        "Hello@World",
        "12345",
        "Test#Case!",
        "   ",
        "Alpha123Beta"
    ]
    for test in test_cases:
        result = has_special_chars(test)
        print(f"{test!r}: {result}")