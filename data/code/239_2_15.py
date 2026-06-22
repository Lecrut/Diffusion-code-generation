RECTANGLE_PERIMETER_CONSTANT = 2

def calculate_rectangle_perimeter(length, width):
    return RECTANGLE_PERIMETER_CONSTANT * (length + width)

if __name__ == '__main__':
    length = 10
    width = 5
    perimeter = calculate_rectangle_perimeter(length, width)
    print(perimeter)