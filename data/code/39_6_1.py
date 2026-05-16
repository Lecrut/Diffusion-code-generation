def find_all_substring_occurrences(text, pattern):
    occurrences = []
    n = len(text)
    m = len(pattern)
    if m == 0:
        return occurrences
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            occurrences.append((i, i + m))
    return occurrences
if __name__ == '__main__':
    text_sample = "abababa"
    pattern_sample = "aba"
    result = find_all_substring_occurrences(text_sample, pattern_sample)
    print(result)
    text_sample_2 = "aaaaa"
    pattern_sample_2 = "aa"
    result_2 = find_all_substring_occurrences(text_sample_2, pattern_sample_2)
    print(result_2)
    text_sample_3 = "banana"
    pattern_sample_3 = "ana"
    result_3 = find_all_substring_occurrences(text_sample_3, pattern_sample_3)
    print(result_3)
    text_sample_4 = "hello world"
    pattern_sample_4 = "l"
    result_4 = find_all_substring_occurrences(text_sample_4, pattern_sample_4)
    print(result_4)