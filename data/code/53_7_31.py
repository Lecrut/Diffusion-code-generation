def calculate_square_area(side_length):
    if side_length < 0:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    test_cases = {
        'tiny': 1,
        'average': 4.2,
        'large': 10,
        'edge_case_zero': 0,
        'invalid_negative': -3
    }
    
    for description, length in test_cases.items():
        try:
            area_result = calculate_square_area(length)
            print(f"The area of a square with {description} side length {length} is {area_result}")
        except ValueError as e:
            print(f"Error calculating area for {description} side length {length}: {e}")