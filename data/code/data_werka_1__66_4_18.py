def check_adjacent_increasing(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list.")
    if not all(isinstance(num, float) for num in numbers):
        raise ValueError("All elements in the list must be floating-point numbers.")
    
    return [numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    sample_values = [3.5, 4.2, 4.8, 5.0, 6.1]
    try:
        result = check_adjacent_increasing(sample_values)
        print(result)
    except (TypeError, ValueError) as e:
        print(e)