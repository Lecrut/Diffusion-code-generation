def calculate_area(dimensions):
    n = len(dimensions)
    if n == 3:
        a, b, c = dimensions
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5
    elif n == 4:
        a, b = (dimensions[0], dimensions[1])
        return a * b
    else:
        x = [dimensions[i] for i in range(0, len(dimensions), 2)]
        y = [dimensions[i] for i in range(1, len(dimensions), 2)]
        area = 0.5 * abs(sum((x[i] * y[(i + 1) % n] - y[i] * x[(i + 1) % n] for i in range(n))))
        return area
if __name__ == '__main__':
    triangle = [3, 4, 5]
    rectangle = [4, 5]
    polygon = [1, 0, 2, 0, 2, 3, 0, 3]
    print('Triangle area:', calculate_area(triangle))
    print('Rectangle area:', calculate_area(rectangle))
    print('Polygon area:', calculate_area(polygon))