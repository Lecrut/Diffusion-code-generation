def calculate_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    area_first = 70
    area_second = 40
    result_difference = calculate_area_difference(area_first, area_second)
    print(result_difference)