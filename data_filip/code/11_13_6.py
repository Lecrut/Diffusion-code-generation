def extract_repeated_characters(text):
    char_counts = {char: text.count(char) for char in text}
    return [char for char, count in char_counts.items() if count > 1]

if __name__ == '__main__':
    sample_text = "hello world"
    result = extract_repeated_characters(sample_text)
    print(result)