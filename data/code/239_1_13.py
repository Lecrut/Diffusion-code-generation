def validate_dimensions(width, height):
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative")

def calculate_rectangle_perimeter(width, height):
    validate_dimensions(width, height)
    return 2 * (width + height)

if __name__ == '__main__':
    width_val = 10
    height_val = 5
    perimeter = calculate_rectangle_perimeter(width_val, height_val)
    print(perimeter)