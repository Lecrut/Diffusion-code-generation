def compute_surface_area():
    length = 10
    width = 8
    height = 6
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    print(compute_surface_area())