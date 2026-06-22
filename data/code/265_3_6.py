class ASCIIExtractor:
    def separate_by_ascii_value(self, phrase):
        even_chars = ''.join(char for char in phrase if ord(char) % 2 == 0)
        odd_chars = ''.join(char for char in phrase if ord(char) % 2 != 0)
        return even_chars, odd_chars

if __name__ == '__main__':
    extractor = ASCIIExtractor()
    sample_phrase = "Hello, World!"
    even, odd = extractor.separate_by_ascii_value(sample_phrase)
    print(even)
    print(odd)