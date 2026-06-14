def calculate_box_properties(dims):
    l, w, h = dims
    surface_area = 2 * (l * w + l * h + w * h)
    volume = l * w * h
    return (surface_area, volume)
if __name__ == '__main__':
    dimensions = [10, 5, 4]
    result = calculate_box_properties(dimensions)
    print(result)