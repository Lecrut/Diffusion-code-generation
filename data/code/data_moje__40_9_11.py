def compute_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    length = 1.5
    width = 2.5
    height = 3.5
    result = compute_surface_area(length, width, height)
    print(result)