import math
def shoelace_area(points):
    if len(points) < 3:
        return 0.0
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    sum1 = 0
    sum2 = 0
    n = len(points)
    for i in range(n):
        j = (i + 1) % n
        sum1 += x[i] * y[j]
        sum2 += y[i] * x[j]
    area = 0.5 * abs(sum1 - sum2)
    return area
if __name__ == '__main__':
    coordinates = [
        (0.0, 0.0),
        (1.0, 0.0),
        (0.0, 1.0),
        (1.0, 1.0),
        (0.5, 0.5)
    ]
    area = shoelace_area(coordinates)
    print(area)