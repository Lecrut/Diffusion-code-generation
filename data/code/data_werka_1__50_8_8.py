def find_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    areas = {
        'area_a': 75,
        'area_b': 30,
        'area_c': 200,
        'area_d': 100,
        'area_e': 5.6,
        'area_f': 3.9
    }
    
    difference_ab = find_area_difference(areas['area_a'], areas['area_b'])
    print(f"The difference between area_a ({areas['area_a']}) and area_b ({areas['area_b']}) is: {difference_ab}")
    
    difference_cd = find_area_difference(areas['area_c'], areas['area_d'])
    print(f"The difference between area_c ({areas['area_c']}) and area_d ({areas['area_d']}) is: {difference_cd}")
    
    difference_ef = find_area_difference(areas['area_e'], areas['area_f'])
    print(f"The difference between area_e ({areas['area_e']}) and area_f ({areas['area_f']}) is: {difference_ef}")