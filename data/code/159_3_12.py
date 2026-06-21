import itertools

class NumberFilter:
    def __init__(self, numbers):
        self.numbers = numbers

    def filter_odd(self):
        return list(itertools.filterfalse(lambda x: x % 2 == 0, self.numbers))

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number_filter = NumberFilter(sample_values)
    odd_numbers = number_filter.filter_odd()
    print(odd_numbers)