def has_repeated_letters(s):
    letter_count = {}
    for char in s:
        if char in letter_count:
            return True
        letter_count[char] = 1
    return False

if __name__ == '__main__':
    test_strings = {
        "hello": True,
        "world": False,
        "programming": True,
        "abcde": False
    }
    
    for string, expected in test_strings.items():
        result = has_repeated_letters(string)
        print(f"'{string}' has repeated letters: {result}")