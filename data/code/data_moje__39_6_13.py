def prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    base_area_value = 50.0
    height_value = 10.0
    volume_result = prism_volume(base_area_value, height_value)
    print(volume_result)