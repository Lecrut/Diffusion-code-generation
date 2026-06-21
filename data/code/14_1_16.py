def has_unique_chars_bitwise(s):
    if len(s) > 128:
        return False
    checker = 0
    for char in s:
        val = ord(char)
        if checker & (1 << val):
            return False
        checker |= (1 << val)
    return True

def static_assertions():
    assert has_unique_chars_bitwise("abcdefg") is True
    assert has_unique_chars_bitwise("hello") is False
    assert has_unique_chars_bitwise("") is True
    assert has_unique_chars_bitwise("a") is True
    assert has_unique_chars_bitwise("aa") is False
    assert has_unique_chars_bitwise("abcdeff") is False
    assert has_unique_chars_bitwise("Python3.9!") is True
    assert has_unique_chars_bitwise("AaBbCcDd") is True
    assert has_unique_chars_bitwise("!!@@##$$") is True
    assert has_unique_chars_bitwise("!!@@##$$!!") is False

if __name__ == '__main__':
    static_assertions()
    sample_strings = ["abcdef", "hello", "unique!", ""]
    for sample in sample_strings:
        print(has_unique_chars_bitwise(sample))