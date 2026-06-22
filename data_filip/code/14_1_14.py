def is_unique(s):
    if len(s) > 128:
        return False
    checker = 0
    for char in s:
        val = ord(char)
        if val > 127:
            return False
        if (checker & (1 << val)) > 0:
            return False
        checker |= 1 << val
    return True

if __name__ == '__main__':
    test_cases = ["abcdef", "hello", "Python", ""]
    for case in test_cases:
        result = is_unique(case)
        print(f"{case}: {result}")
    assert is_unique("abcdef") == True
    assert is_unique("hello") == False
    assert is_unique("") == True
    assert is_unique("Python") == True