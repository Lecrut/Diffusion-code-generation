def has_duplicate_chars(s):
    seen = 0
    for char in s:
        bit = 1 << (ord(char) - ord('a'))
        if seen & bit:
            return True
        seen |= bit
    return False

if __name__ == '__main__':
    test_string = "hello"
    result = has_duplicate_chars(test_string)
    print(result)