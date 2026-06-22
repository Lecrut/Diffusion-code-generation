def is_positive_number(value):
    return isinstance(value, (int, float)) and value > 0

def calculate_triangle_area(base, height):
    if not is_positive_number(base) or not is_positive_number(height):
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    sample_base = 15
    sample_height = 6
    try:
        area = calculate_triangle_area(sample_base, sample_height)
        print(f"The area of the triangle is: {area}")
    except ValueError as e:
        print(e)