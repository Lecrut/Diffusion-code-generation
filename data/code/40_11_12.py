def compute_cuboid_surface_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    sample_length = 5
    sample_width = 3
    sample_height = 4
    print(compute_cuboid_surface_area(sample_length, sample_width, sample_height))