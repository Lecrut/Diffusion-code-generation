def is_strictly_increasing(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, float) for x in numbers):
        raise ValueError("Input must be a list of floating-point numbers.")
    
    comparisons = []
    for i in range(len(numbers) - 1):
        comparisons.append(numbers[i] < numbers[i + 1])
    
    return comparisons

if __name__ == '__main__':
    sample_values = [3.5, 4.0, 4.5, 5.2, 6.1]
    try:
        result = is_strictly_increasing(sample_values)
        print(result)
    except ValueError as e:
        print(e)