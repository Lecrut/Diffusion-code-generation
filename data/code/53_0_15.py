def calculate_square_area(side_length):
    return side_length * side_length

if __name__ == '__main__':
    test_cases = [
        {'side': 3, 'expected': 9},
        {'side': 6, 'expected': 36},
        {'side': 0, 'expected': 0}
    ]
    
    for case in test_cases:
        side_length = case['side']
        area = calculate_square_area(side_length)
        print(f"The area of a square with side length {side_length} is {area}.")