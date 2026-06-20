def find_duplicate_chars(text):
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    duplicates = []
    for char, count in char_counts.items():
        if count > 1:
            duplicates.append(char)
    
    duplicates.sort()
    return duplicates

if __name__ == '__main__':
    sample_text = "programming"
    result = find_duplicate_chars(sample_text)
    print(result)