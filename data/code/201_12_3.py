def calculate_mean(numbers):
    if not all(isinstance(num, float) for num in numbers):
        raise TypeError("All elements in the iterable must be floats")
    total = sum(numbers)
    count = len(numbers)
    return total / count

if __name__ == '__main__':
    sample_values = [1.0, 2.0, 3.0, 4.0, 5.0]
    result = calculate_mean(sample_values)
    print(result)