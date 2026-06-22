PERIMETER_FACTOR = 2

def calculate_perimeter(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return PERIMETER_FACTOR * (length + width)

if __name__ == '__main__':
    length = 6
    width = 2
    print(calculate_perimeter(length, width))