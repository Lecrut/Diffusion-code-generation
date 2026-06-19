def find_substring_occurrences(text, pattern):
    if not pattern:
        return []
    pattern_length = len(pattern)
    text_length = len(text)
    occurrences = []
    for i in range(text_length - pattern_length + 1):
        if text[i:i + pattern_length] == pattern:
            occurrences.append((i, i + pattern_length))
    return occurrences
if __name__ == '__main__':
    sample_text = 'hello world, hello universe'
    search_pattern = 'hello'
    result = find_substring_occurrences(sample_text, search_pattern)
    print(result)
    another_sample_text = 'abracadabra'
    another_search_pattern = 'bra'
    another_result = find_substring_occurrences(another_sample_text, another_search_pattern)
    print(another_result)