def compare_areas(shape1, shape2):
    area1 = shape1[0] * shape1[1]
    area2 = shape2[0] * shape2[1]
    return area1, area2
if __name__ == '__main__':
    shape_a = (5, 10)
    shape_b = (4, 8)
    area_a, area_b = compare_areas(shape_a, shape_b)
    print(f"Area of shape A: {area_a}")
    print(f"Area of shape B: {area_b}")
    shape_c = (6, 3)
    shape_d = (5, 10)
    area_c, area_d = compare_areas(shape_c, shape_d)
    print(f"Area of shape C: {area_c}")
    print(f"Area of shape D: {area_d}")