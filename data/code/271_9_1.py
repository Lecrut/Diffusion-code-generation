def categorize_characters(text):
    char_counts = {}
    for char in text:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts
if __name__ == '__main__':
    sample_text = "Hello World! This is a test string."
    result = categorize_characters(sample_text)
    print(result)