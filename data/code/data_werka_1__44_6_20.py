PERIMETER_MULTIPLIER = 2

def calculate_perimeter(length, width):
    return PERIMETER_MULTIPLIER * (length + width)

if __name__ == '__main__':
    length = 10
    width = 4
    print(calculate_perimeter(length, width))