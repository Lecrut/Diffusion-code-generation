def calculate_area_difference(area1, area2):
    return abs(area1 - area2)
if __name__ == '__main__':
    area_a = 25.5
    area_b = 15.0
    difference = calculate_area_difference(area_a, area_b)
    print(f"The difference between {area_a} and {area_b} is: {difference}")
    area_c = 100
    area_d = 100
    difference2 = calculate_area_difference(area_c, area_d)
    print(f"The difference between {area_c} and {area_d} is: {difference2}")
    area_e = 3.14159
    area_f = 2.71828
    difference3 = calculate_area_difference(area_e, area_f)
    print(f"The difference between {area_e} and {area_f} is: {difference3}")