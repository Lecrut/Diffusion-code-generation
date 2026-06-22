def calculate_surface_area(dimensions):
    width, height, depth = dimensions
    return 2 * (width * height + height * depth + depth * width)

if __name__ == '__main__':
    sample_dimensions = (1.5, 2.5, 3.5)
    result = calculate_surface_area(sample_dimensions)
    print(result)