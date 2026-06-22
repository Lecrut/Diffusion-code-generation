def compare_strings(str1, str2):
    CASE_INSENSITIVE_COMPARISON = lambda s1, s2: s1.lower() == s2.lower()
    return CASE_INSENSITIVE_COMPARISON(str1, str2)

if __name__ == '__main__':
    SAMPLE_STR1 = "Hello"
    SAMPLE_STR2 = "hello"
    result = compare_strings(SAMPLE_STR1, SAMPLE_STR2)
    print(result)

    ANOTHER_SAMPLE1 = "Python"
    ANOTHER_SAMPLE2 = "PYTHON"
    another_result = compare_strings(ANOTHER_SAMPLE1, ANOTHER_SAMPLE2)
    print(another_result)

    FINAL_SAMPLE1 = "World"
    FINAL_SAMPLE2 = "world!"
    final_result = compare_strings(FINAL_SAMPLE1, FINAL_SAMPLE2)
    print(final_result)