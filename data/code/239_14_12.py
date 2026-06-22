def calculate_rectangle_perimeter(width, height):
    if width < 0 or height < 0:
        raise ValueError("Width and height must be non-negative numbers.")
    return 2 * (width + height)

if __name__ == '__main__':
    try:
        sample_width = 5
        sample_height = 3
        perimeter = calculate_rectangle_perimeter(sample_width, sample_height)
        print(perimeter)
    except ValueError as e:
        print(e)