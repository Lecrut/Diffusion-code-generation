def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    triangle_base = 15
    triangle_height = 6
    try:
        area_result = calculate_triangle_area(triangle_base, triangle_height)
        print(f"The area of the triangle with base {triangle_base} and height {triangle_height} is: {area_result}")
    except ValueError as e:
        print(e)