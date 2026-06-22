def is_strictly_increasing(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, float) for x in numbers):
        raise ValueError("Input must be a list of floating-point numbers.")
    
    return [numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    sample_values = [0.1, 0.2, 0.3, 0.4, 0.5]
    try:
        result = is_strictly_increasing(sample_values)
        print(result)
    except ValueError as e:
        print(e)