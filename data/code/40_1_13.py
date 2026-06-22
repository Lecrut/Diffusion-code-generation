def compute_rectangular_prism_surface_area(length, width, height):
    area = 2 * (length * width + width * height + height * length)
    return area

if __name__ == '__main__':
    length = 5.0
    width = 3.0
    height = 2.0
    result = compute_rectangular_prism_surface_area(length, width, height)
    print(result)