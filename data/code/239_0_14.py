PERIMETER_CONSTANT = 2

def calculate_perimeter(width, height):
    return PERIMETER_CONSTANT * (width + height)

if __name__ == '__main__':
    width = 5
    height = 3
    perimeter = calculate_perimeter(width, height)
    print(perimeter)