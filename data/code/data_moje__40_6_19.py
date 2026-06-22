def calculate_rectangular_prism_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    l = 5.5
    w = 3.2
    h = 7.1
    result = calculate_rectangular_prism_surface_area(l, w, h)
    print(result)