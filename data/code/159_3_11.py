import itertools

def filter_odd_numbers(numbers):
    return list(itertools.filterfalse(lambda x: x % 2 == 0, numbers))

if __name__ == '__main__':
    sample_values = [12, 15, 22, 33, 44, 55]
    odd_numbers = filter_odd_numbers(sample_values)
    print(odd_numbers)