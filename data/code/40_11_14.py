def total_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    print(total_surface_area(3, 4, 5))