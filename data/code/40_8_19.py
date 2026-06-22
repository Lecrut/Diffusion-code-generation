def calculate_surface_area(width, height, depth):
    return 2 * (width * height + width * depth + height * depth)

if __name__ == '__main__':
    w = 3
    h = 4
    d = 5
    print(calculate_surface_area(w, h, d))