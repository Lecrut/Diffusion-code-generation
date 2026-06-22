def has_unique_chars(s):
    if len(s) > 128:
        return False
    checker = 0
    for char in s:
        val = ord(char)
        if (checker & (1 << val)) != 0:
            return False
        checker |= (1 << val)
    return True

def assert_static():
    assert has_unique_chars("abcdef") is True
    assert has_unique_chars("abcde f") is True
    assert has_unique_chars("hello") is False
    assert has_unique_chars("") is True
    assert has_unique_chars("a") is True
    assert has_unique_chars("aa") is False
    assert has_unique_chars("abacdfg") is False
    assert has_unique_chars("abcdefg") is True

if __name__ == '__main__':
    assert_static()
    print(has_unique_chars("hello"))
    print(has_unique_chars("world"))
    print(has_unique_chars("abcdef"))
    print(has_unique_chars("abcdea"))