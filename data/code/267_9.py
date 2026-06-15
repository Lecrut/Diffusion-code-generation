def check_string(s):
    is_long = len(s) > 10
    is_alpha = s.isalpha()
    return (is_long, is_alpha)
if __name__ == '__main__':
    test_strings = [
        "short",
        "thisisalongstring",
        "onlyletters",
        "this has a space",
        "abcdefghij",
        "a" * 11,
        "1234567890"
    ]
    for s in test_strings:
        result = check_string(s)
        print(f"Input: '{s}', Result: {result}")