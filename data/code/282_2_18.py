def sum_sequence(numbers):
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the sequence must be numbers")
    return sum(numbers)

if __name__ == '__main__':
    sample_values = [10, 20, 30, 40, 50]
    result = sum_sequence(sample_values)
    print(result)