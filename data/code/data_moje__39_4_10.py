def prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    sample_base = 25.0
    sample_height = 10.0
    print(prism_volume(sample_base, sample_height))