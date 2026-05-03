def find_area_difference(area1, area2):
    result = area1 - area2
    return result
if __name__ == '__main__':
    area_a = 50
    area_b = 25
    difference = find_area_difference(area_a, area_b)
    print(f"The difference between {area_a} and {area_b} is: {difference}")
    area_c = 100
    area_d = 150
    difference2 = find_area_difference(area_c, area_d)
    print(f"The difference between {area_c} and {area_d} is: {difference2}")