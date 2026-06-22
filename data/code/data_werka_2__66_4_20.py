def is_strictly_increasing(numbers):
    if not isinstance(numbers, list) or not all(isinstance(x, float) for x in numbers):
        raise ValueError("Input must be a list of floating-point numbers.")
    
    def compare_adjacent(a, b):
        return a < b
    
    result = []
    for i in range(len(numbers) - 1):
        result.append(compare_adjacent(numbers[i], numbers[i + 1]))
    
    return result

if __name__ == '__main__':
    sample_values = [3.5, 4.0, 5.2, 6.7, 8.0]
    try:
        result = is_strictly_increasing(sample_values)
        print(result)
    except ValueError as e:
        print(e)