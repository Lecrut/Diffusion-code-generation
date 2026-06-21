import itertools

def filter_odd_numbers(numbers):
    return list(itertools.filterfalse(lambda x: x % 2 == 0, numbers))

if __name__ == '__main__':
    sample_values = [10, 23, 45, 68, 90, 11]
    odd_numbers = filter_odd_numbers(sample_values)
    print(odd_numbers)