class OddNumberFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def filter_odds(self):
        return [num for num in self.numbers if num % 2 != 0]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_filter = OddNumberFilter(sample_numbers)
    odd_numbers = odd_filter.filter_odds()
    print(odd_numbers)