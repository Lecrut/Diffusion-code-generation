def has_unique_chars(s):
    if len(s) == 0:
        return True
    sorted_chars = sorted(s)
    for i in range(1, len(sorted_chars)):
        if sorted_chars[i] == sorted_chars[i - 1]:
            return False
    return True

if __name__ == '__main__':
    sample1 = "abcdefg"
    sample2 = "hello"
    sample3 = ""
    sample4 = "a"
    print(has_unique_chars(sample1))
    print(has_unique_chars(sample2))
    print(has_unique_chars(sample3))
    print(has_unique_chars(sample4))