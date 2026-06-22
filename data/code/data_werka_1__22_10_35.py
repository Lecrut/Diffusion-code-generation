class OddNumberFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def filter_odds(self):
        return [num for num in self.numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_numbers = [17, 42, 5, 8, 9, 10, 13]
    odd_filter = OddNumberFilter(sample_numbers)
    print(odd_filter.filter_odds())