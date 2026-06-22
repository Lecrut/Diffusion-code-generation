def are_all_chars_distinct(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    sample_string_1 = "abcdef"
    sample_string_2 = "aabbcc"
    sample_string_3 = "Hello"
    result_1 = are_all_chars_distinct(sample_string_1)
    result_2 = are_all_chars_distinct(sample_string_2)
    result_3 = are_all_chars_distinct(sample_string_3)
    print(result_1)
    print(result_2)
    print(result_3)