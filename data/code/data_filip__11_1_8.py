def find_duplicate_characters(text):
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    duplicates = [char for char, count in char_counts.items() if count > 1]
    return sorted(duplicates)

if __name__ == '__main__':
    sample_text = "abracadabra"
    result = find_duplicate_characters(sample_text)
    print(result)