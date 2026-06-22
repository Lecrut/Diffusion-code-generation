def validate_tuple_elements(input_tuple):
    for element in input_tuple:
        if not isinstance(element, float):
            raise ValueError("All elements in the tuple must be floating-point numbers.")

def calculate_difference(numbers):
    validate_tuple_elements(numbers)
    return max(numbers) - min(numbers)

if __name__ == '__main__':
    sample_numbers = (3.5, 7.2, 1.8, 9.0, 4.6)
    try:
        difference = calculate_difference(sample_numbers)
        print(difference)
    except ValueError as e:
        print(f"Error: {e}")