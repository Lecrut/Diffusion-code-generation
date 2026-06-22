def has_duplicate_chars(s):
    bitmask = 0
    for char in s:
        index = ord(char) - ord('a')
        if (bitmask & (1 << index)) != 0:
            return True
        bitmask |= (1 << index)
    return False

if __name__ == '__main__':
    test_string = "hello"
    result = has_duplicate_chars(test_string)
    print(result)