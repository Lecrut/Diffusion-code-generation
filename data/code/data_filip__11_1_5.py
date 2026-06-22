def find_duplicate_characters(text):
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    duplicates = [char for char, count in char_count.items() if count > 1]
    return sorted(duplicates)

if __name__ == '__main__':
    sample_text = "hello world"
    result = find_duplicate_characters(sample_text)
    print(result)