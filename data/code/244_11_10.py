def sum_areas(side1, side2):
    area1 = side1 ** 2
    area2 = side2 ** 2
    return area1 + area2

if __name__ == '__main__':
    s1 = 5
    s2 = 3
    result = sum_areas(s1, s2)
    print(result)