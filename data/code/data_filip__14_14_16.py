def has_unique_chars(s):
    if not s:
        return True
    sorted_s = sorted(s)
    for i in range(1, len(sorted_s)):
        if sorted_s[i] == sorted_s[i - 1]:
            return False
    return True

if __name__ == '__main__':
    sample_string = "abcdefg"
    sample_string_duplicate = "hello"
    result1 = has_unique_chars(sample_string)
    result2 = has_unique_chars(sample_string_duplicate)
    print(result1)
    print(result2)