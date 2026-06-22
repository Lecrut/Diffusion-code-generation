def compute_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    length = 6
    width = 4
    perimeter = compute_rectangle_perimeter(length, width)
    print(perimeter)