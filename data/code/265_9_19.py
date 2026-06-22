def extract_perfect_square_ascii_chars(phrase):
    result = ''.join(char for char in phrase if (ord(char) ** 0.5).is_integer())
    return result

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    print(extract_perfect_square_ascii_chars(sample_phrase))