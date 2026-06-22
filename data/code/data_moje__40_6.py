def rectangular_prism_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 5.0
    width = 3.0
    height = 4.0
    result = rectangular_prism_surface_area(length, width, height)
    print(result)