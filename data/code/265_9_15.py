class AsciiSquareExtractor:
    @staticmethod
    def is_perfect_square(n):
        return int(n**0.5) ** 2 == n

    @staticmethod
    def extract(s):
        result = []
        for char in s:
            if AsciiSquareExtractor.is_perfect_square(ord(char)):
                result.append(char)
        return ''.join(result)

if __name__ == '__main__':
    extractor = AsciiSquareExtractor()
    print(extractor.extract("a1b2c3d4e5"))