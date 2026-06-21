class OddNumberExtractor:
    @staticmethod
    def extract_odd_numbers(numbers):
        return tuple(x for x in numbers if x % 2 != 0)

if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
    odd_numbers = OddNumberExtractor.extract_odd_numbers(sample_tuple)
    print(odd_numbers)