def is_ascii_even(char):
    return ord(char) % 2 == 0

def separate_by_ascii_value(phrase):
    even_chars = ''.join(filter(is_ascii_even, phrase))
    odd_chars = ''.join((char for char in phrase if not is_ascii_even(char)))
    return (even_chars, odd_chars)
if __name__ == '__main__':
    sample_phrase = 'Hello, World!'
    even, odd = separate_by_ascii_value(sample_phrase)
    print(even)
    print(odd)