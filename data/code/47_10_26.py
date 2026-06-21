TRIANGLE_BASE = 15
TRIANGLE_HEIGHT = 10

def calculate_triangle_area(base, height):
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")
    return 0.5 * base * height

if __name__ == '__main__':
    try:
        area_result = calculate_triangle_area(TRIANGLE_BASE, TRIANGLE_HEIGHT)
        print(area_result)
    except ValueError as e:
        print(e)