def calculate_triangle_area(base, height):
    if base <= 0:
        raise ValueError("Base must be a positive number.")
    if height <= 0:
        raise ValueError("Height must be a positive number.")
    return 0.5 * base * height

if __name__ == '__main__':
    SAMPLE_BASE = 15
    SAMPLE_HEIGHT = 6
    try:
        area = calculate_triangle_area(SAMPLE_BASE, SAMPLE_HEIGHT)
        print(area)
    except ValueError as e:
        print(e)