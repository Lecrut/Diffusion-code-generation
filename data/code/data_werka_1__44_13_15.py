def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    length = 10
    width = 5
    perimeter = calculate_rectangle_perimeter(length, width)
    print(perimeter)