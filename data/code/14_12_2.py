def has_unique_chars(s):
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if val < 0 or val > 25:
            continue
        if checker & (1 << val):
            return False
        checker |= (1 << val)
    return True

if __name__ == '__main__':
    test_string_1 = "hello"
    test_string_2 = "world"
    test_string_3 = "python"
    print(has_unique_chars(test_string_1))
    print(has_unique_chars(test_string_2))
    print(has_unique_chars(test_string_3))