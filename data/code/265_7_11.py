class PrimeCharExtractor:
    @staticmethod
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    @classmethod
    def extract(cls, phrase):
        return ''.join(char for index, char in enumerate(phrase, start=1) if cls.is_prime(index))

if __name__ == '__main__':
    sample_phrase = "Hello, World!"
    extractor = PrimeCharExtractor()
    result = extractor.extract(sample_phrase)
    print(result)