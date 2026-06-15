import math
def compare_areas(area1: float, area2: float) -> str:
    if area1 > area2:
        return f"Shape 1 has a larger area ({area1:.4f} vs {area2:.4f})"
    elif area2 > area1:
        return f"Shape 2 has a larger area ({area2:.4f} vs {area1:.4f})"
    else:
        return f"Both shapes have equal areas ({area1:.4f})"
if __name__ == '__main__':
    shape_a_area = 10.56789
    shape_b_area = 10.56788
    print(compare_areas(shape_a_area, shape_b_area))
    shape_c_area = 42.0
    shape_d_area = 39.99999999999999
    print(compare_areas(shape_c_area, shape_d_area))
    shape_e_area = 5.123
    shape_f_area = 5.123
    print(compare_areas(shape_e_area, shape_f_area))