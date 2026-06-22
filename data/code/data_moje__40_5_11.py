def compute_surface_area(width, height, depth):
    return 2 * (width * height + width * depth + height * depth)

if __name__ == '__main__':
    result = compute_surface_area(10, 8, 6)
    print(result)