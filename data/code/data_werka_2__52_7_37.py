AREA_FACTOR = 0.5

def calculate_triangle_area(x1, y1):
    return abs(AREA_FACTOR * (x1 * 0 + y1 * 0 - 0 * y1 - 0 * x1))
if __name__ == '__main__':
    sample_x = 5
    sample_y = 12
    area = calculate_triangle_area(sample_x, sample_y)
    print(area)