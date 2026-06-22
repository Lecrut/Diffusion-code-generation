def calculate_rectangle_perimeter(width=7, height=4):
    return 2 * (width + height)

if __name__ == '__main__':
    width = 10
    height = 6
    perimeter = calculate_rectangle_perimeter(width, height)
    print(perimeter)