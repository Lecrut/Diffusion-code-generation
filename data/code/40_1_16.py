def compute_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 5.0
    width = 3.0
    height = 2.0
    result = compute_surface_area(length, width, height)
    print(result)