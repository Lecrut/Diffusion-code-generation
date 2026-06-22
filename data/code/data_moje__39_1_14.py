def compute_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    base_area_value = 10.5
    height_value = 4.2
    result = compute_prism_volume(base_area_value, height_value)
    print(result)