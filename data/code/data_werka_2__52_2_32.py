def calculate_triangle_area(base, height):
    if base <= 0:
        raise ValueError("Base must be a positive number.")
    if height <= 0:
        raise ValueError("Height must be a positive number.")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        sample_base = 10
        sample_height = 4
        area = calculate_triangle_area(sample_base, sample_height)
        print(f"The area of the triangle with base {sample_base} and height {sample_height} is {area}.")
    except ValueError as e:
        print(e)