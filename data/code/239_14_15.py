WIDTH = 5
HEIGHT = 3

def calculate_rectangle_perimeter(width, height):
    return 2 * (width + height)
if __name__ == '__main__':
    perimeter = calculate_rectangle_perimeter(WIDTH, HEIGHT)
    print(perimeter)