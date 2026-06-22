class AsciiSeparator:
    def separate_even_odd(self, phrase):
        even_chars = ''.join(char for char in phrase if ord(char) % 2 == 0)
        odd_chars = ''.join(char for char in phrase if ord(char) % 2 != 0)
        return even_chars, odd_chars

if __name__ == '__main__':
    separator = AsciiSeparator()
    sample_phrase1 = "Hello, World!"
    even, odd = separator.separate_even_odd(sample_phrase1)
    print(even)
    print(odd)

    sample_phrase2 = "Python3.8"
    even, odd = separator.separate_even_odd(sample_phrase2)
    print(even)
    print(odd)