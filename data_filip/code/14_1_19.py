def are_chars_unique(s):
    checker = 0
    for char in s:
        val = ord(char)
        if (checker & (1 << val)) != 0:
            return False
        checker |= (1 << val)
    return True

def static_assert():
    assert are_chars_unique("") is True
    assert are_chars_unique("a") is True
    assert are_chars_unique("ab") is True
    assert are_chars_unique("aa") is False
    assert are_chars_unique("abcde") is True
    assert are_chars_unique("hello") is False
    assert are_chars_unique("world") is False
    assert are_chars_unique("python") is True

if __name__ == '__main__':
    static_assert()
    print(are_chars_unique("abcdefg"))
    print(are_chars_unique("hello world"))
    print(are_chars_unique("unique"))