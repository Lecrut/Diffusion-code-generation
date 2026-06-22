def surface_area_of_rectangular_box(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    print(surface_area_of_rectangular_box(1.5, 2.5, 3.5))