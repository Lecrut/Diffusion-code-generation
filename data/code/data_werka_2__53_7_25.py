SQUARE_AREA_THRESHOLD = 0

def calculate_square_area(side_length):
    if side_length < SQUARE_AREA_THRESHOLD:
        raise ValueError("Side length cannot be negative")
    return side_length * side_length

if __name__ == '__main__':
    test_cases = [
        {'label': 'small', 'value': 3},
        {'label': 'medium', 'value': 5.5},
        {'label': 'zero', 'value': 0},
        {'label': 'negative', 'value': -2}
    ]
    
    for case in test_cases:
        try:
            area = calculate_square_area(case['value'])
            print(f"The area of a square with {case['label']} side length {case['value']} is {area}")
        except ValueError as e:
            print(e)