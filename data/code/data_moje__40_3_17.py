def calculate_surface_area(dimensions):
    length, width, height = dimensions
    return 2.0 * (length * width + width * height + height * length)

if __name__ == '__main__':
    sample_dimensions = (10.0, 5.0, 2.5)
    result = calculate_surface_area(sample_dimensions)
    print(result)