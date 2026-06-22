PERIMETER_MULTIPLIER = 2

def calculate_perimeter(length, width):
    return PERIMETER_MULTIPLIER * (length + width)
if __name__ == '__main__':
    LENGTH_VALUE = 5
    WIDTH_VALUE = 3
    print(calculate_perimeter(LENGTH_VALUE, WIDTH_VALUE))