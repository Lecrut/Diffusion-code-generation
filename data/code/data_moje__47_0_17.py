def arithmetic_mean(numbers):
    if not numbers:
        raise ValueError("Cannot calculate mean of an empty list")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [10.5, 20.3, 30.2, 40.0, 50.1]
    result = arithmetic_mean(sample_values)
    print(result)