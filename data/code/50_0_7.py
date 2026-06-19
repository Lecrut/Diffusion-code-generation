def calculate_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    areas = {'area1': 80, 'area2': 20}
    difference = calculate_area_difference(areas['area1'], areas['area2'])
    print(difference)