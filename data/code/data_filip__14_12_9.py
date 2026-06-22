def has_duplicate_characters(s):
    seen = 0
    for char in s:
        bit = 1 << (ord(char) - ord('a'))
        if seen & bit:
            return True
        seen |= bit
    return False

if __name__ == '__main__':
    print(has_duplicate_characters("hello"))
    print(has_duplicate_characters("world"))
    print(has_duplicate_characters("python"))