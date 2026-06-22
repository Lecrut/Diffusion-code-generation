PERIMETER_CONSTANT = 2

def calculate_perimeter(length, width):
    return PERIMETER_CONSTANT * (length + width)

if __name__ == '__main__':
    length = 5
    width = 3
    print(calculate_perimeter(length, width))