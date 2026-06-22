def find_duplicate_characters(text):
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    
    duplicates = []
    for char, count in char_counts.items():
        if count > 1:
            duplicates.append(char)
    
    duplicates.sort()
    return duplicates

if __name__ == '__main__':
    sample_text = "programming"
    result = find_duplicate_characters(sample_text)
    print(result)