def calculate_square_area(side_length):
    if not isinstance(side_length, (int, float)):
        raise ValueError("Side length must be a numeric value.")
    return side_length * side_length

if __name__ == '__main__':
    test_values = {
        'integer_side': 3,
        'float_side': 4.5,
        'invalid_input': 'a'
    }
    
    for key, value in test_values.items():
        try:
            area = calculate_square_area(value)
            print(f"The area of the square with {key} side length is: {area}")
        except ValueError as e:
            print(f"Error calculating area for {key}: {e}")