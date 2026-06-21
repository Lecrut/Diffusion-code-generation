class OddNumberExtractor:
    @staticmethod
    def extract_odds(data):
        return tuple(num for num in data if num % 2 != 0)

if __name__ == '__main__':
    sample_sequence = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    odd_numbers = OddNumberExtractor.extract_odds(sample_sequence)
    print(odd_numbers)