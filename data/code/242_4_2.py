def calculate_and_compare_areas(shape1, shape2):
    area1 = shape1[0] * shape1[1]
    area2 = shape2[0] * shape2[1]
    comparison = "Area 1 is greater" if area1 > area2 else ("Area 1 is less" if area1 < area2 else "Areas are equal")
    return area1, area2, comparison
if __name__ == '__main__':
    shape_a = (5, 10)
    shape_b = (4, 8)
    area_a, area_b, comparison_result = calculate_and_compare_areas(shape_a, shape_b)
    print(f"Shape A dimensions: {shape_a}, Area: {area_a}")
    print(f"Shape B dimensions: {shape_b}, Area: {area_b}")
    print(f"Comparison: {comparison_result}")
    shape_c = (6, 6)
    shape_d = (5, 5)
    area_c, area_d, comparison_result2 = calculate_and_compare_areas(shape_c, shape_d)
    print(f"\nShape C dimensions: {shape_c}, Area: {area_c}")
    print(f"Shape D dimensions: {shape_d}, Area: {area_d}")
    print(f"Comparison: {comparison_result2}")
    shape_e = (10, 10)
    shape_f = (10, 10)
    area_e, area_f, comparison_result3 = calculate_and_compare_areas(shape_e, shape_f)
    print(f"\nShape E dimensions: {shape_e}, Area: {area_e}")
    print(f"Shape F dimensions: {shape_f}, Area: {area_f}")
    print(f"Comparison: {comparison_result3}")