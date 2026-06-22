def calculate_surface_area(dimensions):
    l, w, h = dimensions
    return 2.0 * (l * w + w * h + h * l)

if __name__ == '__main__':
    dims = (3.0, 4.0, 5.0)
    area = calculate_surface_area(dims)
    print(area)