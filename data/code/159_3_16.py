import itertools

def filter_odd_numbers(numbers):
    return list(itertools.filterfalse(lambda x: x % 2 == 0, numbers))

class OddNumberFilter:
    def __init__(self, numbers):
        self.numbers = numbers
    
    def get_odd_numbers(self):
        return filter_odd_numbers(self.numbers)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_filter = OddNumberFilter(sample_values)
    print(odd_filter.get_odd_numbers())