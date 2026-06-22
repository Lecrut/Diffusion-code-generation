class PrimeCharExtractor:
    PRIME_NUMBERS = set(range(2, 100))

    @staticmethod
    def is_prime(n):
        if n in PrimeCharExtractor.PRIME_NUMBERS:
            return True
        if n <= 1 or (n % 2 == 0 and n > 2):
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    @staticmethod
    def extract_prime_position_chars(phrase):
        return ''.join((char for index, char in enumerate(phrase, start=1) if PrimeCharExtractor.is_prime(index)))
if __name__ == '__main__':
    sample_phrase = 'Hello, World!'
    print(PrimeCharExtractor.extract_prime_position_chars(sample_phrase))