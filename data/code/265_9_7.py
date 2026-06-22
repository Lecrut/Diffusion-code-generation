def extract_perfect_square_ascii_chars(phrase):
    return ''.join(char for char in phrase if (ord(char) ** 0.5).is_integer())

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    result = extract_perfect_square_ascii_chars(sample_phrase)
    print(result)