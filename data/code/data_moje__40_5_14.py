def calculate_surface_area(width, height, depth):
    return 2 * (width * height + width * depth + height * depth)

if __name__ == '__main__':
    width = 10
    height = 8
    depth = 6
    print(calculate_surface_area(width, height, depth))