def has_unique_chars(s):
    checker = 0
    for char in s:
        val = ord(char)
        if val >= 128:
            return False
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True

if __name__ == '__main__':
    test_string = "abcdefg"
    result = has_unique_chars(test_string)
    assert result is True
    print(f"String '{test_string}' has unique characters: {result}")
    test_string_duplicate = "abcdeff"
    result_duplicate = has_unique_chars(test_string_duplicate)
    assert result_duplicate is False
    print(f"String '{test_string_duplicate}' has unique characters: {result_duplicate}")