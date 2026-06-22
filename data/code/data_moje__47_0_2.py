def calculate_arithmetic_mean(numbers):
    if len(numbers) == 0:
        raise ValueError("Cannot calculate mean of an empty list")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.5, 2.5, 3.0, 4.0, 5.0]
    result = calculate_arithmetic_mean(sample_values)
    print(result)