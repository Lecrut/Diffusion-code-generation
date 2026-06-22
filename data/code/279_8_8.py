def cycle_and_square(numbers):
    return [num ** 2 for num in numbers]

if __name__ == '__main__':
    sample_values = [1, 2, 3, 4, 5]
    print(cycle_and_square(sample_values))