def has_duplicate_chars(s):
    check = 0
    for char in s:
        val = ord(char) - ord('a')
        if (check & (1 << val)) != 0:
            return True
        check |= (1 << val)
    return False

if __name__ == '__main__':
    print(has_duplicate_chars("abcdefg"))
    print(has_duplicate_chars("hello"))
    print(has_duplicate_chars("algorithm"))
    print(has_duplicate_chars(""))