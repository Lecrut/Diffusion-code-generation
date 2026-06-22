def has_unique_chars_sorting(s):
    if not s:
        return True
    sorted_chars = sorted(s)
    for i in range(len(sorted_chars) - 1):
        if sorted_chars[i] == sorted_chars[i + 1]:
            return False
    return True

if __name__ == '__main__':
    sample1 = "abcdef"
    sample2 = "hello"
    sample3 = ""
    sample4 = "a"

    print(has_unique_chars_sorting(sample1))
    print(has_unique_chars_sorting(sample2))
    print(has_unique_chars_sorting(sample3))
    print(has_unique_chars_sorting(sample4))