PERIMETER_COEFFICIENT = 2

def calculate_perimeter(width, height):
    return PERIMETER_COEFFICIENT * (width + height)

if __name__ == '__main__':
    WIDTH = 5
    HEIGHT = 3
    perimeter = calculate_perimeter(WIDTH, HEIGHT)
    print(perimeter)