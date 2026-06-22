def calculate_prism_volume(base_area, height):
    volume_result = base_area * height
    return volume_result

if __name__ == '__main__':
    area_val = 20.5
    h_val = 12.3
    computed_volume = calculate_prism_volume(area_val, h_val)
    print(computed_volume)