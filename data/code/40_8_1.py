def surface_area_of_box(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    result = surface_area_of_box(3, 4, 5)
    print(result)