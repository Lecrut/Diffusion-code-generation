def has_duplicate_chars_bitwise(s):
    if not s:
        return False
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if (checker & (1 << val)) != 0:
            return True
        checker |= (1 << val)
    return False

if __name__ == '__main__':
    print(has_duplicate_chars_bitwise("abcd"))
    print(has_duplicate_chars_bitwise("abca"))
    print(has_duplicate_chars_bitwise(""))
    print(has_duplicate_chars_bitwise("hello"))