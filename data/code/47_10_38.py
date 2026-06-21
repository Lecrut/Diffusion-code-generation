TRIANGLE_HALF = 0.5

def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return TRIANGLE_HALF * base * height

if __name__ == '__main__':
    SAMPLE_BASE = 15
    SAMPLE_HEIGHT = 6
    try:
        area_result = calculate_triangle_area(SAMPLE_BASE, SAMPLE_HEIGHT)
        print(area_result)
    except ValueError as e:
        print(e)