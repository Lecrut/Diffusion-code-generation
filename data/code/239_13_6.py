PERIMETER_MULTIPLIER = 2

def calculate_perimeter(length, width):
    return PERIMETER_MULTIPLIER * (length + width)

if __name__ == '__main__':
    LENGTH = 5
    WIDTH = 3
    print(calculate_perimeter(LENGTH, WIDTH))