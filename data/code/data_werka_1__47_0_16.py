def calculate_triangle_area(base, height):
    try:
        if not isinstance(base, (float, int)) or not isinstance(height, (float, int)):
            raise TypeError("Both base and height must be numbers.")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        return 0.5 * base * height
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    sample_values = {
        'base': 12.0,
        'height': 6.0
    }
    
    area = calculate_triangle_area(sample_values['base'], sample_values['height'])
    if area is not None:
        print(area)