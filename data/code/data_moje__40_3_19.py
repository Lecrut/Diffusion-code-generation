def calculate_surface_area(dims):
    l, w, h = dims
    return 2.0 * (l * w + w * h + h * l)

if __name__ == '__main__':
    dimensions = (1.0, 2.0, 3.0)
    area = calculate_surface_area(dimensions)
    print(area)