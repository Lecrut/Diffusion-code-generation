def has_unique_chars(s):
    if len(s) > 128:
        return False
    checker = 0
    for char in s:
        val = ord(char)
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True

assert has_unique_chars("abcdefg") == True
assert has_unique_chars("hello") == False

if __name__ == '__main__':
    test_strings = ["abcdefg", "hello", "world", "a", ""]
    for s in test_strings:
        result = has_unique_chars(s)
        print(f"{repr(s)}: {result}")