PERIMETER_FACTOR = 2

def calculate_rectangle_perimeter(width, height):
    return PERIMETER_FACTOR * (width + height)

if __name__ == '__main__':
    width_val = 10
    height_val = 5
    perimeter = calculate_rectangle_perimeter(width_val, height_val)
    print(perimeter)