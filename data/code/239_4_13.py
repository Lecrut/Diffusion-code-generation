PERIMETER_FACTOR = 2

def calculate_rectangle_perimeter(width, height):
    return PERIMETER_FACTOR * (width + height)
if __name__ == '__main__':
    width = 5
    height = 3
    print(calculate_rectangle_perimeter(width, height))