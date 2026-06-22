def calculate_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    sample_length = 3.0
    sample_width = 4.0
    sample_height = 5.0
    area = calculate_surface_area(sample_length, sample_width, sample_height)
    print(area)