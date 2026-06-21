def calculate_mean(numbers):
    if not isinstance(numbers, list) or len(numbers) == 0:
        raise ValueError("Input must be a non-empty list of floats")
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

if __name__ == '__main__':
    sample_values = [2.1, 3.9, 5.7, 6.3]
    result = calculate_mean(sample_values)
    print(result)