def compute_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    dims = (10, 8, 6)
    print(compute_surface_area(*dims))