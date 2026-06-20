def perform_operations(numbers):
    results = []
    for i in range(len(numbers) - 1):
        addition = numbers[i] + numbers[i + 1]
        subtraction = numbers[i] - numbers[i + 1]
        results.append((addition, subtraction))
    return results

if __name__ == '__main__':
    sample_numbers = [10, 5, 3, 8]
    print(perform_operations(sample_numbers))