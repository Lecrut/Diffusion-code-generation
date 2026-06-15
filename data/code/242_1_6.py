import math
def compare_areas(area1, area2):
    if area1 > area2:
        return f"Shape with area {area1} has a larger area."
    elif area2 > area1:
        return f"Shape with area {area2} has a larger area."
    else:
        return "Both shapes have equal areas."
if __name__ == '__main__':
    area_a = 10.56789
    area_b = 10.567890000000001
    area_c = 5.0
    area_d = 12.345
    print(f"Comparing {area_a} and {area_b}: {compare_areas(area_a, area_b)}")
    print(f"Comparing {area_c} and {area_d}: {compare_areas(area_c, area_d)}")
    print(f"Comparing {area_a} and {area_c}: {compare_areas(area_a, area_c)}")
    print(f"Comparing {area_b} and {area_d}: {compare_areas(area_b, area_d)}")