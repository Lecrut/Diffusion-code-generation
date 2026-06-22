def find_substring_indices(text, pattern):
    indices = []
    n = len(text)
    m = len(pattern)
    if m == 0:
        return indices
    
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            indices.append((i, i + m))
    
    return indices

if __name__ == '__main__':
    SAMPLE_TEXT = "hello world, hello universe"
    SEARCH_PATTERN = "hello"
    result = find_substring_indices(SAMPLE_TEXT, SEARCH_PATTERN)
    print(result)