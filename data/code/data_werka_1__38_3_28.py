def has_repeated_letters(s):
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    return False

if __name__ == '__main__':
    test_strings = ["hello", "world", "abcde", "programming"]
    for test_string in test_strings:
        print(f"'{test_string}' has repeated letters: {has_repeated_letters(test_string)}")