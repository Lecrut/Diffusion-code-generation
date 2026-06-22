def calculate_mean(numbers):
    if not numbers:
        raise ValueError('The list of numbers cannot be empty.')
    total = sum(numbers)
    count = len(numbers)
    return total / count
if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    mean_value = calculate_mean(sample_numbers)
    print(mean_value)