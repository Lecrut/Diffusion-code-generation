import itertools

def is_even(number):
    return number % 2 == 0

def filter_odd_numbers(numbers):
    return list(itertools.filterfalse(is_even, numbers))

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filter_odd_numbers(sample_values))