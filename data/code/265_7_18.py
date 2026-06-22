class PrimeCharExtractor:
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def extract_chars(self, phrase):
        return ''.join(char for index, char in enumerate(phrase, start=1) if self.is_prime(index))

if __name__ == '__main__':
    extractor = PrimeCharExtractor()
    sample_phrase = "Hello, World!"
    print(extractor.extract_chars(sample_phrase))