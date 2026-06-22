def calculate_surface_area(width, height, depth):
    return 2 * (width * height + width * depth + height * depth)

if __name__ == '__main__':
    w, h, d = 3, 4, 5
    result = calculate_surface_area(w, h, d)
    print(result)