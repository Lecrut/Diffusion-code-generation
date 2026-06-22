def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        base = 12.0
        height = 8.0
        area = calculate_triangle_area(base, height)
        print(f"Area of triangle with base {base} and height {height}: {area}")
    except ValueError as e:
        print(e)