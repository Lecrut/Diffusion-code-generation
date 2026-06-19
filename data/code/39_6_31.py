def find_all_occurrences(text, pattern):
    if not pattern:
        return []
    
    occurrences = []
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            occurrences.append((i, i + m))
    
    return occurrences

if __name__ == '__main__':
    sample_text = "abracadabra"
    sample_pattern = "abra"
    print(find_all_occurrences(sample_text, sample_pattern))
    
    sample_text_2 = "hello world, hello universe"
    sample_pattern_2 = "hello"
    print(find_all_occurrences(sample_text_2, sample_pattern_2))