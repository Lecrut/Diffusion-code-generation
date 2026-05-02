def calculate_area_difference(area1, area2):
    return abs(area1 - area2)
if __name__ == '__main__':
    area_a = 10.5
    area_b = 5.2
    result1 = calculate_area_difference(area_a, area_b)
    print(result1)
    area_c = 100
    area_d = 98
    result2 = calculate_area_difference(area_c, area_d)
    print(result2)
    area_e = 3.14159
    area_f = 3.14158
    result3 = calculate_area_difference(area_e, area_f)
    print(result3)