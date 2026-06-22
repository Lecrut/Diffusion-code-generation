def cycle_and_square(numbers):
    return [num ** 2 for num in numbers]

if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    squared_numbers = cycle_and_square(sample_numbers)
    print(squared_numbers)