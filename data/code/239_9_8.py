def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    length = 7
    width = 4
    perimeter = calculate_rectangle_perimeter(length, width)
    print(perimeter)