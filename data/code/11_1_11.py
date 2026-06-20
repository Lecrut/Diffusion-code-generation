def find_duplicate_chars(text):
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    duplicates = [char for char, count in char_count.items() if count > 1]
    return sorted(list(set(duplicates)))

if __name__ == '__main__':
    sample_text = "programming"
    result = find_duplicate_chars(sample_text)
    print(result)