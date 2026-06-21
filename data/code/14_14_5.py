def has_unique_chars(s):
    if not s:
        return True
    sorted_chars = sorted(s)
    for i in range(1, len(sorted_chars)):
        if sorted_chars[i] == sorted_chars[i - 1]:
            return False
    return True

if __name__ == '__main__':
    sample_string_1 = "abcdef"
    sample_string_2 = "hello"
    sample_string_3 = ""
    result_1 = has_unique_chars(sample_string_1)
    result_2 = has_unique_chars(sample_string_2)
    result_3 = has_unique_chars(sample_string_3)
    print(result_1)
    print(result_2)
    print(result_3)