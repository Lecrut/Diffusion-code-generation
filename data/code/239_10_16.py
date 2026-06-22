def calculate_rectangle_perimeter(width, height):
    return 2 * (width + height)

if __name__ == '__main__':
    width = 10
    height = 7
    perimeter = calculate_rectangle_perimeter(width, height)
    print(perimeter)