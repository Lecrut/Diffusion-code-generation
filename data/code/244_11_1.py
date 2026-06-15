def sum_areas(shape1, shape2):
    area1 = shape1[0] * shape1[1]
    area2 = shape2[0] * shape2[1]
    return area1 + area2
if __name__ == '__main__':
    s1 = (10, 5)
    s2 = (3, 8)
    result = sum_areas(s1, s2)
    print(result)