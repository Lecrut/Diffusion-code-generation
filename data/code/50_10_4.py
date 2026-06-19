def calculate_area_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    area_a = 50
    area_b = 30
    difference = calculate_area_difference(area_a, area_b)
    print(difference)