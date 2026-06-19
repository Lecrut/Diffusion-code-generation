RECTANGLE_PERIMETER_FACTOR = 2

def calculate_perimeter(length, width):
    return RECTANGLE_PERIMETER_FACTOR * (length + width)

if __name__ == '__main__':
    length = 15.0
    width = 7.0
    perimeter = calculate_perimeter(length, width)
    print(f"Length: {length}")
    print(f"Width: {width}")
    print(f"Perimeter: {perimeter}")