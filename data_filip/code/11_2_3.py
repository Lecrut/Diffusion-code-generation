def extract_repeated_characters(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    repeated_chars = set()
    for char, count in char_counts.items():
        if count > 1:
            repeated_chars.add(char)
    return sorted(list(repeated_chars))

if __name__ == '__main__':
    sample_string = "programming"
    result = extract_repeated_characters(sample_string)
    print(result)