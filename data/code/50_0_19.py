def calculate_area_difference(area1, area2):
    difference = abs(area1 - area2)
    return difference

if __name__ == '__main__':
    areas = {'area1': 80, 'area2': 20}
    result = calculate_area_difference(areas['area1'], areas['area2'])
    print(result)