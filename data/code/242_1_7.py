import math
def compare_areas(area1, area2):
    if area1 > area2:
        return f"Shape with area {area1} has a larger area than the other shape with area {area2}."
    elif area2 > area1:
        return f"Shape with area {area2} has a larger area than the other shape with area {area1}."
    else:
        return f"Both shapes have equal areas of {area1}."
if __name__ == '__main__':
    area_a = 10.56789
    area_b = 10.56788
    print(compare_areas(area_a, area_b))
    area_c = 42.0
    area_d = 39.99999999999999
    print(compare_areas(area_c, area_d))
    area_e = 5.123
    area_f = 5.123
    print(compare_areas(area_e, area_f))