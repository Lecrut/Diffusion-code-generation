def cycle_and_square(numbers):
    squared_values = [num ** 2 for num in numbers]
    return squared_values

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = cycle_and_square(sample_values)
    print(result)