EVEN_CHAR = "even_chars"
ODD_CHAR = "odd_chars"

def separate_by_ascii_value(phrase):
    even_chars = ''.join(char for char in phrase if ord(char) % 2 == 0)
    odd_chars = ''.join(char for char in phrase if ord(char) % 2 != 0)
    return {EVEN_CHAR: even_chars, ODD_CHAR: odd_chars}

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    result = separate_by_ascii_value(sample_phrase)
    print(result)