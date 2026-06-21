def calculate_mean(numbers):
    if not isinstance(numbers, list) or len(numbers) == 0:
        raise ValueError("Input must be a non-empty list of floats")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.8, 2.2, 3.4, 4.6]
    result = calculate_mean(sample_values)
    print(result)