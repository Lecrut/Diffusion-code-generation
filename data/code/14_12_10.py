def has_duplicate_chars(s):
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if checker & (1 << val):
            return True
        checker |= 1 << val
    return False

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "abca"
    print(has_duplicate_chars(test_string_1))
    print(has_duplicate_chars(test_string_2))