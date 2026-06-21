import itertools

class EvenNumberExtractor:
    @staticmethod
    def extract_even_numbers(start, stop):
        return list(itertools.islice(range(start, stop + 1), 0, None, 2))

if __name__ == '__main__':
    even_numbers = EvenNumberExtractor.extract_even_numbers(1, 30)
    print(f"Even numbers: {even_numbers}")