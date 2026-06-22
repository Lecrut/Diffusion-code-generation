def extract_repeated_chars(text):
    char_counts = {char: text.count(char) for char in set(text)}
    return [char for char, count in sorted(char_counts.items()) if count > 1]

if __name__ == '__main__':
    sample_text = "programming"
    result = extract_repeated_chars(sample_text)
    print(result)