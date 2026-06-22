SQUARE_SIDE = 5
TRIANGLE_BASE = 4
TRIANGLE_HEIGHT = 6

def calculate_square_area(side):
    return side ** 2

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def compare_areas():
    square_area = calculate_square_area(SQUARE_SIDE)
    triangle_area = calculate_triangle_area(TRIANGLE_BASE, TRIANGLE_HEIGHT)
    return square_area > triangle_area

if __name__ == '__main__':
    print(compare_areas())