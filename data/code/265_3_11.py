def separate_even_odd_ascii(phrase):
    even_chars = ''.join(c for c in phrase if ord(c) % 2 == 0)
    odd_chars = ''.join(c for c in phrase if ord(c) % 2 != 0)
    return even_chars, odd_chars

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    even, odd = separate_even_odd_ascii(sample_phrase)
    print("Even ASCII characters:", even)
    print("Odd ASCII characters:", odd)