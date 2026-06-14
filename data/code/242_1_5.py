import math
def compare_areas(area1: float, area2: float) -> str:
    if area1 > area2:
        return "Shape 1 has a larger area."
    elif area2 > area1:
        return "Shape 2 has a larger area."
    else:
        return "Both shapes have equal areas."
if __name__ == '__main__':
    area_a = 10.56789
    area_b = 10.56789000000001
    area_c = 5.0
    area_d = 5.0
    print(f"Comparing Area A ({area_a}) and Area B ({area_b}): {compare_areas(area_a, area_b)}")
    print(f"Comparing Area C ({area_c}) and Area D ({area_d}): {compare_areas(area_c, area_d)}")
    print(f"Comparing Area A ({area_a}) and Area C ({area_c}): {compare_areas(area_a, area_c)}")