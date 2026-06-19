def calculate_difference(area1, area2):
    return abs(area1 - area2)

if __name__ == '__main__':
    area_a = 300
    area_b = 450
    difference = calculate_difference(area_a, area_b)
    print(difference)