def calculate_rectangle_perimeter(width, height):
    if not all(isinstance(i, (int, float)) and i > 0 for i in [width, height]):
        raise ValueError("Width and height must be positive numbers")
    return 2 * (width + height)

if __name__ == '__main__':
    width_val = 10
    height_val = 5
    perimeter = calculate_rectangle_perimeter(width_val, height_val)
    print(perimeter)