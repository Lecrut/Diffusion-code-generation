def calculate_square_area(side):
    if side <= 0:
        raise ValueError("Side length must be a positive number.")
    return side * side

if __name__ == '__main__':
    test_cases = {
        'positive_integer': 5,
        'positive_float': 10.5,
        'zero': 0,
        'negative': -3
    }
    
    for name, side in test_cases.items():
        try:
            area = calculate_square_area(side)
            print(f"The area of a square with {name} side {side} is: {area}")
        except ValueError as e:
            print(f"Error for {name} side {side}: {e}")