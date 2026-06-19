class OddNumberFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    @staticmethod
    def is_odd(number):
        return number % 2 != 0

    def filter_odds(self):
        return [num for num in self.numbers if self.is_odd(num)]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filter_instance = OddNumberFilter(sample_numbers)
    odd_numbers = filter_instance.filter_odds()
    print(odd_numbers)