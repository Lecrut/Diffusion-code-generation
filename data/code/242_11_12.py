SQUARE_SIDE = 5
TRIANGLE_BASE = 4
TRIANGLE_HEIGHT = 6

def compare_areas():
    area_square = SQUARE_SIDE ** 2
    area_triangle = 0.5 * TRIANGLE_BASE * TRIANGLE_HEIGHT
    return area_square > area_triangle

if __name__ == '__main__':
    print(compare_areas())