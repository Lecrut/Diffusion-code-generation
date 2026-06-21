class OddNumberExtractor:
    def __init__(self, numbers):
        self.numbers = numbers

    def extract_odds(self):
        return tuple(x for x in self.numbers if x % 2 != 0)

if __name__ == '__main__':
    extractor = OddNumberExtractor((1, 2, 3, 4, 5, 6, 7, 8, 9))
    odd_numbers = extractor.extract_odds()
    print(odd_numbers)