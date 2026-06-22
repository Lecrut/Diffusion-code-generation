def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    sample_base_areas = [10, 25, 100, 0, 50]
    sample_heights = [5, 4, 3, 10, 10]

    for base_area, height in zip(sample_base_areas, sample_heights):
        volume = calculate_prism_volume(base_area, height)
        print(volume)