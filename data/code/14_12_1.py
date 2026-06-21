def has_duplicate(s):
    checker = 0
    for c in s:
        val = ord(c) - ord('a')
        if checker & (1 << val):
            return True
        checker |= (1 << val)
    return False

if __name__ == '__main__':
    print(has_duplicate("abc"))
    print(has_duplicate("hello"))
    print(has_duplicate("abcdefg"))
    print(has_duplicate("aabbcc"))