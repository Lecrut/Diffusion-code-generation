def calculate_square_side_length(area):
    if area < 0:
        raise ValueError("Area cannot be negative")
    return area ** 0.5

if __name__ == '__main__':
    test_cases = [
        {'area': 16, 'expected': 4},
        {'area': 25, 'expected': 5},
        {'area': 81, 'expected': 9}
    ]
    
    for case in test_cases:
        side_length = calculate_square_side_length(case['area'])
        print(f"The side length of the square with area {case['area']} is: {side_length}")