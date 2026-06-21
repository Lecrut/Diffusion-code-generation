def validate_input(numbers):
    if not all(isinstance(num, (int, float, str)) for num in numbers):
        raise ValueError("Input must be a list of integers, floats, or strings.")

def convert_to_floats(numbers):
    return [float(num) for num in numbers]

def sort_numbers(numbers):
    return sorted(numbers)

if __name__ == '__main__':
    sample_values = ['3.5', 2, '4', 1.1]
    validate_input(sample_values)
    float_values = convert_to_floats(sample_values)
    sorted_values = sort_numbers(float_values)
    print(sorted_values)