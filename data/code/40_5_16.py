def compute_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 10
    width = 8
    height = 6
    result = compute_surface_area(length, width, height)
    print(result)