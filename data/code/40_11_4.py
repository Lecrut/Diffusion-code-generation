def total_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

if __name__ == '__main__':
    print(total_surface_area(3, 4, 5))