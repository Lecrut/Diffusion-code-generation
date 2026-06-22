def calculate_perimeter(length, width):
    return 2 * (length + width)

if __name__ == '__main__':
    length = 9
    width = 4
    perimeter = calculate_perimeter(length, width)
    print(perimeter)