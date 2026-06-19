def is_strictly_increasing(numbers):
    def validate_input(data):
        if not all(isinstance(x, float) for x in data):
            raise ValueError("All elements must be floating-point numbers.")
    
    validate_input(numbers)
    return [numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    sample_values = [3.0, 4.5, 6.2, 7.8, 9.1]
    result = is_strictly_increasing(sample_values)
    print(result)