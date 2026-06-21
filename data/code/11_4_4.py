def find_duplicate_characters(text: str) -> list:
    char_counts = {}
    lower_text = text.lower()
    for char in lower_text:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    duplicates = [char for char, count in char_counts.items() if count > 1]
    return duplicates

if __name__ == '__main__':
    sample_string = "Programming"
    result = find_duplicate_characters(sample_string)
    print(result)