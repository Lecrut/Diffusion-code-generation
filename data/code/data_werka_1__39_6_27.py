def find_substring_indices(text, pattern):
    if not pattern:
        return []
    
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
    sample_text = "abababa"
    sample_pattern = "aba"
    print(find_substring_indices(sample_text, sample_pattern))
    
    another_text = "aaaaa"
    another_pattern = "aa"
    print(find_substring_indices(another_text, another_pattern))