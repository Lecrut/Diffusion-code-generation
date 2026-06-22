def calculate_rectangle_perimeter(width, height):
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative numbers.")
    return 2 * (width + height)

if __name__ == '__main__':
    print(calculate_rectangle_perimeter(5, 3))