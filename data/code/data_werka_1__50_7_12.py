def calculate_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    areas = {
        'region_a': 120.75,
        'region_b': 85.45
    }
    difference = calculate_area_difference(areas['region_a'], areas['region_b'])
    print(difference)