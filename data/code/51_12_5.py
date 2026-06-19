def calculate_perimeter(width, height):
    return 2 * (width + height)

if __name__ == '__main__':
    width = 5.0
    height = 3.0
    perimeter = calculate_perimeter(width, height)
    print(perimeter)