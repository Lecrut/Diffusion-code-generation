def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == '__main__':
    rect_length = 10
    rect_width = 3
    print(calculate_perimeter(rect_length, rect_width))