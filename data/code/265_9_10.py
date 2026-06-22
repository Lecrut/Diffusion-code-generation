def extract_perfect_square_chars(phrase):
    return ''.join(char for char in phrase if (ord(char) ** 0.5).is_integer())

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    print(extract_perfect_square_chars(sample_phrase))