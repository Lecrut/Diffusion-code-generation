RECTANGLE_PERIMETER_FACTOR = 2

def calculate_rectangle_perimeter(width, height):
    perimeter = RECTANGLE_PERIMETER_FACTOR * (width + height)
    return perimeter

if __name__ == '__main__':
    print(calculate_rectangle_perimeter(10, 5))