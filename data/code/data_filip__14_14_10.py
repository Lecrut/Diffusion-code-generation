def has_unique_chars_sorted(s):
    sorted_chars = sorted(s)
    for i in range(len(sorted_chars) - 1):
        if sorted_chars[i] == sorted_chars[i + 1]:
            return False
    return True

if __name__ == '__main__':
    sample1 = "abcdefg"
    sample2 = "hello"
    sample3 = ""
    sample4 = "a"
    sample5 = "aabbcc"
    print(has_unique_chars_sorted(sample1))
    print(has_unique_chars_sorted(sample2))
    print(has_unique_chars_sorted(sample3))
    print(has_unique_chars_sorted(sample4))
    print(has_unique_chars_sorted(sample5))