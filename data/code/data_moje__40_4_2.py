def calculate_surface_area(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive numbers")
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    sample_length = 5
    sample_width = 3
    sample_height = 4
    result = calculate_surface_area(sample_length, sample_width, sample_height)
    print(result)