def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    test_cases = [
        {'base': 10, 'height': 5},
        {'base': 20, 'height': 8},
        {'base': 30, 'height': 12}
    ]
    
    for case in test_cases:
        try:
            area = calculate_triangle_area(case['base'], case['height'])
            print(f"Area of triangle with base {case['base']} and height {case['height']}: {area}")
        except ValueError as e:
            print(e)