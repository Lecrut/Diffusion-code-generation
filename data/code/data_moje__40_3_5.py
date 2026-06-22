def calculate_surface_area(dimensions):
    l, w, h = dimensions
    return 2 * (l * w + w * h + h * l)

if __name__ == '__main__':
    sample_dimensions = (10.5, 20.2, 30.8)
    result = calculate_surface_area(sample_dimensions)
    print(result)