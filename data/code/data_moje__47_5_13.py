def calculate_mean(numbers):
    if not numbers:
        return 0.0
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_numbers = [10, 20, 30, 40, 50]
    result = calculate_mean(sample_numbers)
    print(result)