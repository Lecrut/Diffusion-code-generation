def find_all_occurrences(text, pattern):
    start_indices = []
    end_indices = []
    n = len(text)
    m = len(pattern)
    if m == 0:
        return []
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            start_indices.append(i)
            end_indices.append(i + m)
    if not start_indices:
        return []
    result = []
    for i in range(len(start_indices)):
        result.append((start_indices[i], end_indices[i]))
    return result
if __name__ == '__main__':
    text_sample = "abababa"
    pattern_sample = "aba"
    result = find_all_occurrences(text_sample, pattern_sample)
    print(result)
    text_sample_2 = "banana"
    pattern_sample_2 = "ana"
    result_2 = find_all_occurrences(text_sample_2, pattern_sample_2)
    print(result_2)
    text_sample_3 = "aaaaa"
    pattern_sample_3 = "aa"
    result_3 = find_all_occurrences(text_sample_3, pattern_sample_3)
    print(result_3)
    text_sample_4 = "hello world"
    pattern_sample_4 = "l"
    result_4 = find_all_occurrences(text_sample_4, pattern_sample_4)
    print(result_4)
    text_sample_5 = "abcde"
    pattern_sample_5 = "xyz"
    result_5 = find_all_occurrences(text_sample_5, pattern_sample_5)
    print(result_5)