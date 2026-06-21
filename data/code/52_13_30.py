def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_values = {
        'triangle1': {'base': 9, 'height': 6},
        'triangle2': {'base': 14, 'height': 3}
    }
    
    for triangle_name, dimensions in sample_values.items():
        area = calculate_triangle_area(dimensions['base'], dimensions['height'])
        print(f"The area of {triangle_name} is: {area}")