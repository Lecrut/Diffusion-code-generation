def calculate_prism_volume(base_area, height):
    return base_area * height

if __name__ == '__main__':
    area1 = 50
    height1 = 10
    result1 = calculate_prism_volume(area1, height1)
    print(result1)
    area2 = 25.5
    height2 = 4
    result2 = calculate_prism_volume(area2, height2)
    print(result2)
    area3 = 0
    height3 = 100
    result3 = calculate_prism_volume(area3, height3)
    print(result3)