def has_unique_characters(s):
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if checker & (1 << val):
            return False
        checker |= 1 << val
    return True

if __name__ == '__main__':
    print(has_unique_characters('abcdef'))
    print(has_unique_characters('abcdea'))