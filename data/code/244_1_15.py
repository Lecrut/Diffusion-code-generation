RECTANGLE_WIDTH = 10
RECTANGLE_HEIGHT = 6
TRIANGLE_BASE = 8
TRIANGLE_HEIGHT = 5

def calculate_rectangle_area(width, height):
    return width * height

def calculate_triangle_area(base, height):
    return 0.5 * base * height

def sum_areas():
    rectangle_area = calculate_rectangle_area(RECTANGLE_WIDTH, RECTANGLE_HEIGHT)
    triangle_area = calculate_triangle_area(TRIANGLE_BASE, TRIANGLE_HEIGHT)
    total_area = rectangle_area + triangle_area
    return total_area
if __name__ == '__main__':
    result = sum_areas()
    print(result)