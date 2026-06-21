def calculate_mean(numbers):
    if not numbers:
        return 0
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_data = [1, 2, 3, 4, 5]
    result = calculate_mean(sample_data)
    print(result)