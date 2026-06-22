def calculate_rectangle_perimeter(width, height):
    if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
        raise ValueError("Width and height must be numbers")
    return 2 * (width + height)

if __name__ == '__main__':
    width_val = 10
    height_val = 5
    perimeter = calculate_rectangle_perimeter(width_val, height_val)
    print(perimeter)