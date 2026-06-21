def calculate_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    triangle_dimensions = {
        'triangle1': {'base': 9, 'height': 4},
        'triangle2': {'base': 15, 'height': 6}
    }
    
    for triangle_name, dimensions in triangle_dimensions.items():
        area = calculate_area(dimensions['base'], dimensions['height'])
        print(f"Area of {triangle_name}: {area}")