def arithmetic_mean(numbers):
    if not numbers:
        raise ValueError("Cannot calculate mean of an empty list")
    return sum(numbers) / len(numbers)

if __name__ == '__main__':
    sample_values = [1.0, 2.5, 3.0, 4.5, 5.0]
    result = arithmetic_mean(sample_values)
    print(result)