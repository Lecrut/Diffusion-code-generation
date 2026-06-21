def extract_repeated_chars(text):
    char_count = {char: text.count(char) for char in set(text)}
    repeated = sorted([char for char, count in char_count.items() if count > 1])
    return repeated
if __name__ == '__main__':
    sample_text = 'programming'
    result = extract_repeated_chars(sample_text)
    print(result)