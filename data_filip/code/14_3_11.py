def has_unique_chars(s):
    if len(s) > 256:
        return False
    sorted_chars = sorted(s)
    i = 1
    length = len(sorted_chars)
    while i < length:
        if sorted_chars[i] == sorted_chars[i - 1]:
            return False
        i += 1
    return True

if __name__ == '__main__':
    sample_string = "abcdefg"
    result = has_unique_chars(sample_string)
    print(result)
    sample_string_dup = "hello"
    result_dup = has_unique_chars(sample_string_dup)
    print(result_dup)