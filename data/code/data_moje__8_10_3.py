import math

def convex_hull_area(points):
    if not points:
        return 0.0
    
    points = sorted(points)
    
    if len(points) <= 1:
        return 0.0
    
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    hull = lower[:-1] + upper[:-1]
    
    if len(hull) < 3:
        return 0.0

    area = 0.0
    n = len(hull)
    for i in range(n):
        j = (i + 1) % n
        area += hull[i][0] * hull[j][1]
        area -= hull[j][0] * hull[i][1]
        
    return abs(area) / 2.0

if __name__ == '__main__':
    pts = [(0, 0), (4, 0), (4, 3), (0, 3)]
    result = convex_hull_area(pts)
    print(result)