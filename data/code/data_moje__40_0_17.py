def calculate_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    sample_length = 5.0
    sample_width = 4.0
    sample_height = 3.0
    result = calculate_surface_area(sample_length, sample_width, sample_height)
    print(result)