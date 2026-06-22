def calculate_surface_area(dimensions):
    length, width, height = dimensions
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    sample_dimensions = (5.0, 3.0, 2.0)
    result = calculate_surface_area(sample_dimensions)
    print(result)