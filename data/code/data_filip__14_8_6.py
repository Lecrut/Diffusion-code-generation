def are_all_chars_distinct(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    sample_string_1 = "abcdefg"
    sample_string_2 = "programming"
    print(are_all_chars_distinct(sample_string_1))
    print(are_all_chars_distinct(sample_string_2))