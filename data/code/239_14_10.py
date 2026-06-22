PERIMETER_MULTIPLIER = 2

def calculate_rectangle_perimeter(width, height):
    return PERIMETER_MULTIPLIER * (width + height)
if __name__ == '__main__':
    width = 5
    height = 3
    perimeter = calculate_rectangle_perimeter(width, height)
    print(perimeter)