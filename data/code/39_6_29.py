def find_substring_indices(text, pattern):
    indices = []
    start = 0
    while True:
        start = text.find(pattern, start)
        if start == -1:
            break
        end = start + len(pattern)
        indices.append((start, end))
        start += 1
    return indices

if __name__ == '__main__':
    TEXT_SAMPLE = "abababa"
    PATTERN_SAMPLE = "aba"
    RESULT = find_substring_indices(TEXT_SAMPLE, PATTERN_SAMPLE)
    print(RESULT)

    TEXT_SAMPLE_2 = "aaaaa"
    PATTERN_SAMPLE_2 = "aa"
    RESULT_2 = find_substring_indices(TEXT_SAMPLE_2, PATTERN_SAMPLE_2)
    print(RESULT_2)