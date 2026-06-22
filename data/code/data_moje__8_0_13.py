def calculate_rectangle_area(length, width):
    try:
        length = float(length)
        width = float(width)
    except (ValueError, TypeError):
        raise ValueError("Length and width must be numeric values")
    
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers")
    
    return length * width

def validate_and_compute(length, width):
    try:
        area = calculate_rectangle_area(length, width)
        return area
    except ValueError as e:
        return str(e)

if __name__ == '__main__':
    sample_length = 5.0
    sample_width = 10.0
    result = validate_and_compute(sample_length, sample_width)
    print(result)
    
    invalid_length = -3
    invalid_width = 4
    error_result = validate_and_compute(invalid_length, invalid_width)
    print(error_result)
    
    non_numeric_length = "abc"
    non_numeric_width = 5
    error_result2 = validate_and_compute(non_numeric_length, non_numeric_width)
    print(error_result2)