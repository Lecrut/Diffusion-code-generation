def has_duplicate(s):
    check = 0
    for c in s:
        val = ord(c) - ord('a')
        if (check & (1 << val)):
            return True
        check |= 1 << val
    return False

if __name__ == '__main__':
    sample1 = "abcde"
    sample2 = "hello"
    print(has_duplicate(sample1))
    print(has_duplicate(sample2))