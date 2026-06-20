def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    side_length = 5
    side_width = 10
    perimeter = calculate_perimeter(side_length, side_width)
    print(perimeter)