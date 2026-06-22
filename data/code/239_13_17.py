def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    rect_length = 7
    rect_width = 4
    perimeter = calculate_perimeter(rect_length, rect_width)
    print(perimeter)