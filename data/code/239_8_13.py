PERIMETER_CONSTANT = 2

def calculate_rectangle_perimeter(width, height):
    return PERIMETER_CONSTANT * (width + height)

if __name__ == '__main__':
    WIDTH_VALUE = 5
    HEIGHT_VALUE = 3
    perimeter = calculate_rectangle_perimeter(WIDTH_VALUE, HEIGHT_VALUE)
    print(perimeter)