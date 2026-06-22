def calculate_area(dimensions):
    n = len(dimensions)
    if n == 3:
        a, b, c = dimensions
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    elif n == 4:
        a, b, c, d = dimensions
        if a == c and b == d:
            return a * b
    x = [dimensions[i] for i in range(0, n, 2)]
    y = [dimensions[i] for i in range(1, n, 2)]
    area = 0.5 * abs((sum(x[i] * y[(i + 1) % len(y)] - y[i] * x[(i + 1) % len(x)]) for i in range(len(x))))
    return area
if __name__ == '__main__':
    triangle = [3, 4, 5]
    rectangle = [4, 5, 4, 5]
    polygon = [1, 0, 2, 0, 2, 3, 1, 3]
    print('Triangle area:', calculate_area(triangle))
    print('Rectangle area:', calculate_area(rectangle))
    print('Polygon area:', calculate_area(polygon))