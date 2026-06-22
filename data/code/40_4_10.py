def calculate_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    sample_length = 10
    sample_width = 5
    sample_height = 3
    area = calculate_surface_area(sample_length, sample_width, sample_height)
    print(area)