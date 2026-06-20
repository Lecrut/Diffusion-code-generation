import math

def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def compute_convex_hull_area(points):
    if len(points) < 3:
        return 0.0
    
    unique_points = list(set(points))
    if len(unique_points) < 3:
        return 0.0
    
    unique_points.sort()
    
    lower = []
    for p in unique_points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(unique_points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    hull = lower[:-1] + upper[:-1]
    
    area = 0.0
    n = len(hull)
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]
    
    return abs(area) / 2.0

if __name__ == '__main__':
    sample_points = [(0, 0), (4, 0), (4, 4), (0, 4), (2, 2), (1, 2)]
    result = compute_convex_hull_area(sample_points)
    print(result)