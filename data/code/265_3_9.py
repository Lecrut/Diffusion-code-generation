def split_by_ascii_value(phrase):
    even_chars = ''.join(c for c in phrase if ord(c) % 2 == 0)
    odd_chars = ''.join(c for c in phrase if ord(c) % 2 != 0)
    return even_chars, odd_chars

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    even, odd = split_by_ascii_value(sample_phrase)
    print("Even ASCII:", even)
    print("Odd ASCII:", odd)