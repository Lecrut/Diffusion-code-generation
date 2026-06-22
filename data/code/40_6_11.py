def rectangular_prism_surface_area(length, width, height):
    if length <= 0 or width <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive numbers.")
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    length = 5.0
    width = 3.0
    height = 4.0
    area = rectangular_prism_surface_area(length, width, height)
    print(area)