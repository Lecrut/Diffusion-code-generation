def filter_numbers(numbers, divisible_by, parity):
    return [num for num in numbers if (num % divisible_by == 0) == parity]
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(filter_numbers(sample_numbers, 2, True))
    print(filter_numbers(sample_numbers, 3, False))