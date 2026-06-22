def prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    sample_base_area = 10.0
    sample_height = 5.0
    volume = prism_volume(sample_base_area, sample_height)
    print(volume)