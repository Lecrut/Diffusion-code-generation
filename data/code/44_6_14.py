def calculate_mean(numbers):
    if not numbers:
        return 0.0
    total = 0.0
    for num in numbers:
        total += num
    return total / len(numbers)

if __name__ == '__main__':
    sample_values = [10.5, 20.3, 30.2, 40.1, 50.0]
    result = calculate_mean(sample_values)
    print(result)