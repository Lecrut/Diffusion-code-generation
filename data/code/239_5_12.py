def calculate_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    rect_length = 8
    rect_width = 4
    perimeter_result = calculate_rectangle_perimeter(rect_length, rect_width)
    print(perimeter_result)