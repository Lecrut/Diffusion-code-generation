def compute_prism_volume(base_area, height):
    if base_area < 0 or height < 0:
        raise ValueError("Base area and height must be non-negative")
    return base_area * height

if __name__ == '__main__':
    base_area_value = 10
    height_value = 5
    result = compute_prism_volume(base_area_value, height_value)
    print(result)
    
    base_area_value_2 = 0
    height_value_2 = 10
    result_2 = compute_prism_volume(base_area_value_2, height_value_2)
    print(result_2)
    
    base_area_value_3 = 7.5
    height_value_3 = 4.2
    result_3 = compute_prism_volume(base_area_value_3, height_value_3)
    print(result_3)