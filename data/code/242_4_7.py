def compare_areas(shape1, shape2):
    area1 = shape1[0] * shape1[1]
    area2 = shape2[0] * shape2[1]
    if area1 > area2:
        return f"Shape 1 area ({area1}) is greater than Shape 2 area ({area2})"
    elif area1 < area2:
        return f"Shape 1 area ({area1}) is less than Shape 2 area ({area2})"
    else:
        return f"Shape 1 area ({area1}) is equal to Shape 2 area ({area2})"
if __name__ == '__main__':
    shape_a = (5, 10)
    shape_b = (4, 12)
    result1 = compare_areas(shape_a, shape_b)
    print(result1)
    shape_c = (7, 3)
    shape_d = (6, 5)
    result2 = compare_areas(shape_c, shape_d)
    print(result2)
    shape_e = (8, 8)
    shape_f = (8, 8)
    result3 = compare_areas(shape_e, shape_f)
    print(result3)