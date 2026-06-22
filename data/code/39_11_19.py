def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    area_1 = 20
    height_1 = 10
    volume_1 = calculate_prism_volume(area_1, height_1)
    print(volume_1)
    
    area_2 = 15.5
    height_2 = 8
    volume_2 = calculate_prism_volume(area_2, height_2)
    print(volume_2)
    
    area_3 = 0
    height_3 = 50
    volume_3 = calculate_prism_volume(area_3, height_3)
    print(volume_3)