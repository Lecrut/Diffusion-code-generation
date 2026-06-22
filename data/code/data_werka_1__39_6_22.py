def find_all_occurrences(text, pattern):
    if not isinstance(text, str) or not isinstance(pattern, str):
        raise ValueError('Both text and pattern must be strings.')
    if len(pattern) == 0:
        return []
    occurrences = []
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        if text[i:i + m] == pattern:
            occurrences.append((i, i + m))
    return occurrences
if __name__ == '__main__':
    try:
        text_sample = 'hello world hello'
        pattern_sample = 'hello'
        result = find_all_occurrences(text_sample, pattern_sample)
        print(result)
        text_sample_2 = 'abcabcabc'
        pattern_sample_2 = 'bca'
        result_2 = find_all_occurrences(text_sample_2, pattern_sample_2)
        print(result_2)
        text_sample_3 = 'mississippi'
        pattern_sample_3 = 'issi'
        result_3 = find_all_occurrences(text_sample_3, pattern_sample_3)
        print(result_3)
    except ValueError as e:
        print(e)