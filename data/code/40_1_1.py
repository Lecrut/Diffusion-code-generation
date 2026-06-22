def compute_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    result = compute_surface_area(5.0, 3.0, 2.0)
    print(result)