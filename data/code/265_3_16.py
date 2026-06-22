def separate_by_ascii_value(phrase):
    even_chars = ''.join(char for char in phrase if ord(char) % 2 == 0)
    odd_chars = ''.join(char for char in phrase if ord(char) % 2 != 0)
    return even_chars, odd_chars

if __name__ == '__main__':
    sample_phrase = "Python 3.8"
    even, odd = separate_by_ascii_value(sample_phrase)
    print(even)
    print(odd)