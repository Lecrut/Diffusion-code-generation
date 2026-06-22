def calculate_surface_area(length, width, height):
    if length < 0 or width < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    sample_length = 5
    sample_width = 3
    sample_height = 4
    area = calculate_surface_area(sample_length, sample_width, sample_height)
    print(area)