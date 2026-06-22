def find_repeated_chars(text):
    char_counts = {}
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated = [char for char, count in char_counts.items() if count > 1]
    return repeated

if __name__ == '__main__':
    sample_text = "aabbccddeeffggh"
    result = find_repeated_chars(sample_text)
    print(result)