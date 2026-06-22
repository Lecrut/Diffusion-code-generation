def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    SAMPLE_BASE = 15
    SAMPLE_HEIGHT = 7
    area = calculate_triangle_area(SAMPLE_BASE, SAMPLE_HEIGHT)
    print(area)