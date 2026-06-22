def total_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    length = 3
    width = 4
    height = 5
    result = total_surface_area(length, width, height)
    print(result)