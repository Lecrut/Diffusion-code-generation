def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    sample_base_area = 12.5
    sample_height = 8.0
    result = calculate_prism_volume(sample_base_area, sample_height)
    print(result)