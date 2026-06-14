def sum_areas(shape1, shape2):
    area1 = shape1[0] * shape1[1]
    area2 = shape2[0] * shape2[1]
    return area1 + area2
if __name__ == '__main__':
    a = (10, 5)
    b = (3, 7)
    result = sum_areas(a, b)
    print(result)