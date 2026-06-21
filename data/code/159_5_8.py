class OddNumberExtractor:
    def __init__(self, data):
        self.data = data

    def extract_odds(self):
        return [num for num in self.data if num % 2 != 0]

if __name__ == '__main__':
    extractor = OddNumberExtractor((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    odd_numbers = extractor.extract_odds()
    print(odd_numbers)