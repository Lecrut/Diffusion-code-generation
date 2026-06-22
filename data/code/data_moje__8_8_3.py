import math

def calculate_convex_hull_area(coordinates):
    if len(coordinates) < 3:
        return 0.0
    
    points = sorted(coordinates, key=lambda p: (p[0], p[1]))
    
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    lower_hull = []
    for p in points:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], p) <= 0:
            lower_hull.pop()
        lower_hull.append(p)
    
    upper_hull = []
    for p in reversed(points):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], p) <= 0:
            upper_hull.pop()
        upper_hull.append(p)
    
    hull = lower_hull[:-1] + upper_hull[:-1]
    
    if len(hull) < 3:
        return 0.0
    
    area = 0.0
    n = len(hull)
    for i in range(n):
        j = (i + 1) % n
        area += (hull[i][0] * hull[j][1]) - (hull[j][0] * hull[i][1])
    
    return abs(area) / 2.0

if __name__ == '__main__':
    coords = [(0, 0), (4, 0), (4, 4), (0, 4), (1, 1)]
    result = calculate_convex_hull_area(coords)
    print(result)