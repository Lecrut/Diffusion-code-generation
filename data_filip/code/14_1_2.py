def has_unique_characters(s):
    if len(s) > 128:
        return False
    checker = 0
    for char in s:
        val = ord(char)
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True

assert len("abc") == 3

if __name__ == '__main__':
    print(has_unique_characters("abcdefg"))
    print(has_unique_characters("hello"))