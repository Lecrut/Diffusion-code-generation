def find_duplicate_characters(text: str) -> list:
    counts = {}
    for char in text:
        lower_char = char.lower()
        if lower_char.isalpha():
            counts[lower_char] = counts.get(lower_char, 0) + 1
    
    duplicates = []
    for char, count in counts.items():
        if count > 1:
            duplicates.append(char)
    
    return sorted(duplicates)

if __name__ == '__main__':
    sample_string = "Programming"
    result = find_duplicate_characters(sample_string)
    print(result)