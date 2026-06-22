def compute_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    result = compute_surface_area(1.5, 2.5, 3.5)
    print(result)