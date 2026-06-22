PERIMETER_FACTOR = 2

def calculate_rectangle_perimeter(length, width):
    return PERIMETER_FACTOR * (length + width)

if __name__ == '__main__':
    length = 5
    width = 3
    perimeter = calculate_rectangle_perimeter(length, width)
    print(perimeter)