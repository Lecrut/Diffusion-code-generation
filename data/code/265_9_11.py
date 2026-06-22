class AsciiSquareFilter:
    ASCII_SQUARES = set(i * i for i in range(1, 26))

    @staticmethod
    def is_ascii_square(value):
        return value in AsciiSquareFilter.ASCII_SQUARES

    @classmethod
    def extract_chars(cls, phrase):
        return ''.join(char for char in phrase if cls.is_ascii_square(ord(char)))

if __name__ == '__main__':
    sample_phrase = "Hello World!"
    print(AsciiSquareFilter.extract_chars(sample_phrase))