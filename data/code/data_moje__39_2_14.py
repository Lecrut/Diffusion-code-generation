def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    sample_base_area = 25.0
    sample_height = 10.0
    volume = calculate_prism_volume(sample_base_area, sample_height)
    print(volume)