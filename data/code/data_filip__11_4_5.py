def find_duplicate_chars(text):
    if not text:
        return []
    
    lower_text = text.lower()
    char_counts = {}
    
    for char in lower_text:
        if char not in char_counts:
            char_counts[char] = 0
        char_counts[char] += 1
    
    duplicates = []
    seen = set()
    
    for char in lower_text:
        if char_counts[char] > 1 and char not in seen:
            duplicates.append(char)
            seen.add(char)
            
    return duplicates

if __name__ == '__main__':
    sample_text = "Hello World"
    result = find_duplicate_chars(sample_text)
    print(result)