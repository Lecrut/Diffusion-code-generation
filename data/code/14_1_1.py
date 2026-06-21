def check_unique_chars_bitwise(s):
    if not s:
        return True
    checker = 0
    for char in s:
        code = ord(char)
        if 0 <= code <= 127:
            if checker & (1 << code):
                return False
            checker |= (1 << code)
        else:
            return False
    return True

def static_assertions():
    assert check_unique_chars_bitwise("abc") is True
    assert check_unique_chars_bitwise("aba") is False
    assert check_unique_chars_bitwise("") is True
    assert check_unique_chars_bitwise("z") is True
    assert check_unique_chars_bitwise("abab") is False
    assert check_unique_chars_bitwise("abcdefg") is True
    assert check_unique_chars_bitwise("hello") is False

if __name__ == '__main__':
    static_assertions()
    print(check_unique_chars_bitwise("abc"))
    print(check_unique_chars_bitwise("aba"))
    print(check_unique_chars_bitwise(""))
    print(check_unique_chars_bitwise("z"))
    print(check_unique_chars_bitwise("abab"))
    print(check_unique_chars_bitwise("abcdefg"))
    print(check_unique_chars_bitwise("hello"))