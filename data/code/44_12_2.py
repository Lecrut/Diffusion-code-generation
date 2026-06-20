def compute_rectangle_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    length = 5
    width = 3
    perimeter = compute_rectangle_perimeter(length, width)
    print(perimeter)