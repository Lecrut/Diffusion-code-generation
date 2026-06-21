import itertools

def exclude_even_numbers(numbers):
    return list(itertools.filterfalse(lambda x: x % 2 == 0, numbers))

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    odd_numbers = exclude_even_numbers(sample_values)
    print(odd_numbers)