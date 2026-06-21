def is_positive_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number.")
    if value <= 0:
        raise ValueError("Value must be positive.")

def calculate_triangle_area(base, height):
    is_positive_number(base)
    is_positive_number(height)
    return 0.5 * base * height

if __name__ == '__main__':
    base = 15
    height = 6
    area = calculate_triangle_area(base, height)
    print(f"The area of the triangle with base {base} and height {height} is: {area}")