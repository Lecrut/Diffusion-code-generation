def find_all_occurrences(text, pattern):
    if not pattern:
        return []
    
    occurrences = []
    text_length = len(text)
    pattern_length = len(pattern)
    
    for i in range(text_length - pattern_length + 1):
        if text[i:i+pattern_length] == pattern:
            occurrences.append((i, i + pattern_length))
    
    return occurrences

if __name__ == '__main__':
    SAMPLE_TEXT = "abababa"
    SAMPLE_PATTERN = "aba"
    print(find_all_occurrences(SAMPLE_TEXT, SAMPLE_PATTERN))
    
    ANOTHER_SAMPLE_TEXT = "aaaaa"
    ANOTHER_SAMPLE_PATTERN = "aa"
    print(find_all_occurrences(ANOTHER_SAMPLE_TEXT, ANOTHER_SAMPLE_PATTERN))