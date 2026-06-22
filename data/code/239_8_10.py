def calculate_rectangle_perimeter(width=5, height=3):
    return 2 * (width + height)

if __name__ == '__main__':
    width = 5
    height = 3
    perimeter = calculate_rectangle_perimeter(width, height)
    print(perimeter)