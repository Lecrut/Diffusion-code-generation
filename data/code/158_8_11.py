from itertools import islice

class NumberExtractor:
    def __init__(self):
        self.range_data = range(1, 31)

    def get_even_numbers(self):
        return list(islice(self.range_data, 1, None, 2))

if __name__ == '__main__':
    extractor = NumberExtractor()
    even_numbers = extractor.get_even_numbers()
    print(f"Even numbers: {even_numbers}")