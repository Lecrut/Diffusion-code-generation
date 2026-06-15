def compare_areas(shape1, shape2):
    area1 = shape1[0] * shape1[1]
    area2 = shape2[0] * shape2[1]
    comparison = "Equal" if area1 == area2 else (f"Shape 1 area ({area1}) is greater than Shape 2 area ({area2})" if area1 > area2 else f"Shape 1 area ({area1}) is less than Shape 2 area ({area2})")
    return area1, area2, comparison
if __name__ == '__main__':
    shape_a = (5, 10)
    shape_b = (4, 15)
    shape_c = (5, 10)
    area_a, area_b, comparison_ab = compare_areas(shape_a, shape_b)
    print(f"Comparing {shape_a} and {shape_b}: Area A = {area_a}, Area B = {area_b}. Result: {comparison_ab}")
    area_a, area_c, comparison_ac = compare_areas(shape_a, shape_c)
    print(f"Comparing {shape_a} and {shape_c}: Area A = {area_a}, Area C = {area_c}. Result: {comparison_ac}")
    shape_d = (6, 8)
    shape_e = (10, 12)
    area_d, area_e, comparison_de = compare_areas(shape_d, shape_e)
    print(f"Comparing {shape_d} and {shape_e}: Area D = {area_d}, Area E = {area_e}. Result: {comparison_de}")