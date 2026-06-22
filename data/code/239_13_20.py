def compute_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    rect_length = 7
    rect_width = 4
    result = compute_rectangle_perimeter(rect_length, rect_width)
    print(result)