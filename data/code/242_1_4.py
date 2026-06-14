import math
def compare_areas(area1, area2):
    if area1 > area2:
        return f"Shape 1 has a larger area ({area1} vs {area2})"
    elif area2 > area1:
        return f"Shape 2 has a larger area ({area2} vs {area1})"
    else:
        return f"Both shapes have equal areas ({area1})"
if __name__ == '__main__':
    area_a = 10.56789
    area_b = 10.567890000000001
    area_c = 5.0
    area_d = 4.999999999999999
    print(compare_areas(area_a, area_b))
    print(compare_areas(area_c, area_d))
    print(compare_areas(area_a, area_c))
    print(compare_areas(area_b, area_d))