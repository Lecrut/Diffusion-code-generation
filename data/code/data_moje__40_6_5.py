def calculate_rectangular_prism_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    sample_length = 5.5
    sample_width = 3.2
    sample_height = 4.0
    result = calculate_rectangular_prism_surface_area(sample_length, sample_width, sample_height)
    print(result)