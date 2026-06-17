def calculate_surface_area(dimensions):
    length, width, height = dimensions
    area = 2 * (length * width + length * height + width * height)
    return area
if __name__ == '__main__':
    box_dimensions = (10, 5, 4)
    surface_area = calculate_surface_area(box_dimensions)
    print(surface_area)