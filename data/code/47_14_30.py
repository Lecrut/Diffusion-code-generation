def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_values = {
        'triangle1': {'base': 10, 'height': 5},
        'triangle2': {'base': 7, 'height': 3}
    }
    
    for name, values in sample_values.items():
        try:
            area = calculate_triangle_area(values['base'], values['height'])
            print(f"Area of {name}: {area}")
        except (TypeError, ValueError) as e:
            print(f"Error calculating area for {name}: {e}")