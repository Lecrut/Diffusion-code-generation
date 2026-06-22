def has_duplicate_bitwise(s):
    if len(s) > 26:
        return True
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if checker & (1 << val):
            return True
        checker |= (1 << val)
    return False

if __name__ == '__main__':
    print(has_duplicate_bitwise('abc'))
    print(has_duplicate_bitwise('hello'))
    print(has_duplicate_bitwise('abcdefghijklmnopqrstuvwxyz'))
    print(has_duplicate_bitwise('abcdefghijklmnopqrstuvwxyza'))