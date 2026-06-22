def find_duplicate_frequencies(text):
    if not text:
        return []
    
    frequency_map = {}
    for char in text:
        frequency_map[char] = frequency_map.get(char, 0) + 1
    
    reverse_map = {}
    for char, count in frequency_map.items():
        if count not in reverse_map:
            reverse_map[count] = []
        reverse_map[count].append(char)
    
    duplicates = []
    for count, chars in reverse_map.items():
        if len(chars) > 1:
            duplicates.extend(chars)
    
    return sorted(duplicates)

if __name__ == '__main__':
    sample_text = "hello world"
    result = find_duplicate_frequencies(sample_text)
    print(result)