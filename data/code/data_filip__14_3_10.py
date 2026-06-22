def is_unique_sorted(s):
    if len(s) <= 1:
        return True
    sorted_chars = sorted(s)
    for i in range(1, len(sorted_chars)):
        if sorted_chars[i] == sorted_chars[i - 1]:
            return False
    return True

if __name__ == '__main__':
    sample_string_1 = "abcdef"
    sample_string_2 = "hello"
    result_1 = is_unique_sorted(sample_string_1)
    result_2 = is_unique_sorted(sample_string_2)
    print(result_1)
    print(result_2)