def surface_area_rectangular_prism(length, width, height):
    return 2 * (length * width + width * height + height * length)

if __name__ == '__main__':
    sample_length = 2.5
    sample_width = 3.0
    sample_height = 4.5
    result = surface_area_rectangular_prism(sample_length, sample_width, sample_height)
    print(result)