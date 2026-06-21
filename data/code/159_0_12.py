class NumberFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def filter_odds(self):
        return list(filter(lambda x: x % 2 != 0, self.numbers))

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    filter_instance = NumberFilter(sample_numbers)
    odd_numbers = filter_instance.filter_odds()
    print(odd_numbers)