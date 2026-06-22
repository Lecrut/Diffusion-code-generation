def surface_area_of_rectangular_box(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 5
    width = 4
    height = 3
    result = surface_area_of_rectangular_box(length, width, height)
    print(result)