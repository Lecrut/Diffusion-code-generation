def extract_unique_chars(phrase):
    unique_chars = []
    for char in phrase:
        if char not in unique_chars:
            unique_chars.append(char)
    return unique_chars

if __name__ == '__main__':
    sample_phrase = "hello world"
    print(extract_unique_chars(sample_phrase))