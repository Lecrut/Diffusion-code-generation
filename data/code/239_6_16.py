def calculate_rectangle_perimeter(width, height):
    if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
        raise TypeError("Width and height must be numeric values.")
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative.")
    return 2 * (width + height)

if __name__ == '__main__':
    print(calculate_rectangle_perimeter(10, 5))