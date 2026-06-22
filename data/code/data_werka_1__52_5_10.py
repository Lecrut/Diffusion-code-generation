def calculate_area(dimensions):
    n = len(dimensions)
    if n == 3:
        return 0.5 * dimensions[0] * dimensions[1]
    elif n == 4 and dimensions[0] == dimensions[2] and (dimensions[1] == dimensions[3]):
        return dimensions[0] * dimensions[1]
    else:
        area = 0
        for i in range(n):
            j = (i + 1) % n
            area += dimensions[i][0] * dimensions[j][1]
            area -= dimensions[j][0] * dimensions[i][1]
        return abs(area) / 2
if __name__ == '__main__':
    triangle = [3, 4]
    rectangle = [5, 6, 5, 6]
    polygon = [(0, 0), (4, 0), (4, 3), (0, 3)]
    print('Triangle area:', calculate_area(triangle))
    print('Rectangle area:', calculate_area(rectangle))
    print('Polygon area:', calculate_area(polygon))