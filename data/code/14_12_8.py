def has_unique_characters(s):
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if checker & (1 << val):
            return False
        checker |= 1 << val
    return True

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "hello"
    print(has_unique_characters(test_string_1))
    print(has_unique_characters(test_string_2))