import math
def calculate_sum_of_areas(poly1_dims, poly2_dims):
    area1 = lambda d: 0.5 * d[0] * d[1]
    area2 = lambda d: 10 * d[0] + d[1]
    total_area = area1(poly1_dims) + area2(poly2_dims)
    return total_area
if __name__ == '__main__':
    polygon1 = (10, 5)
    polygon2 = (4, 8)
    result = calculate_sum_of_areas(polygon1, polygon2)
    print(result)