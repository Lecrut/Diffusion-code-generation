PERIMETER_MULTIPLIER = 2

def calculate_rectangle_perimeter(length, width):
    return PERIMETER_MULTIPLIER * (length + width)

if __name__ == '__main__':
    length = 5
    width = 3
    print(calculate_rectangle_perimeter(length, width))