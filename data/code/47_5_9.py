def calculate_mean(numbers):
    if not numbers:
        raise ValueError('List must not be empty')
    total = sum(numbers)
    count = len(numbers)
    return total / count
if __name__ == '__main__':
    sample_numbers = [1, 2, 3, 4, 5]
    result = calculate_mean(sample_numbers)
    print(result)