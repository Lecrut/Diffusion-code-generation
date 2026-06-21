def filter_odd_numbers(numbers):
    if not isinstance(numbers, (list, tuple, set)):
        raise ValueError("Input must be an iterable of numbers")
    return list(filter(lambda x: x % 2 != 0, numbers))

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filter_odd_numbers(sample_values))