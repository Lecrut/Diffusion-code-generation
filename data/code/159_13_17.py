class NumberFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def filter_odds(self):
        return tuple(x for x in self.numbers if x % 2 != 0)

if __name__ == '__main__':
    sample_tuple = (10, 23, 45, 68, 90, 113)
    filter_instance = NumberFilter(sample_tuple)
    odd_numbers = filter_instance.filter_odds()
    print(odd_numbers)