def validate_positive_number(value):
    if value <= 0:
        raise ValueError("Value must be positive.")

def calculate_triangle_area(base, height):
    validate_positive_number(base)
    validate_positive_number(height)
    return 0.5 * base * height

if __name__ == '__main__':
    base = 25
    height = 15
    area = calculate_triangle_area(base, height)
    print(area)