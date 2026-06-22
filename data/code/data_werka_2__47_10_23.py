def calculate_triangle_area(base, height):
    return 0.5 * base * height

if __name__ == '__main__':
    TRIANGLE_BASE = 8
    TRIANGLE_HEIGHT = 12
    area_result = calculate_triangle_area(TRIANGLE_BASE, TRIANGLE_HEIGHT)
    print(area_result)