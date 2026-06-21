def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    test_cases = {
        'case1': {'base': 30, 'height': 20},
        'case2': {'base': 18, 'height': 12},
        'case3': {'base': 7, 'height': 5}
    }
    
    for case_name, values in test_cases.items():
        area = calculate_triangle_area(values['base'], values['height'])
        print(f"Area of triangle {case_name}: {area}")