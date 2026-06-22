def is_unique_chars(input_str):
    if len(input_str) > 128:
        return False
    checker = 0
    for char in input_str:
        val = ord(char)
        if val > 127:
            return False
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True

if __name__ == '__main__':
    sample_strings = ["abcdef", "hello", "123456", "aa"]
    for s in sample_strings:
        print(is_unique_chars(s))
    assert is_unique_chars("abcdef") is True
    assert is_unique_chars("hello") is False
    assert is_unique_chars("123456") is True
    assert is_unique_chars("aa") is False
    assert is_unique_chars("") is True
    assert is_unique_chars("AaBbCc") is True