def compute_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    l = 5.0
    w = 3.0
    h = 2.0
    result = compute_surface_area(l, w, h)
    print(result)