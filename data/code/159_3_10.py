import itertools

def is_odd(x):
    return x % 2 != 0

def filter_odd_numbers(numbers):
    return list(itertools.filterfalse(is_even, numbers))

def is_even(x):
    return not is_odd(x)

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_numbers = filter_odd_numbers(sample_values)
    print(odd_numbers)