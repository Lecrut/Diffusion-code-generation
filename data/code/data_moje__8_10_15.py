import math

def convex_hull_area(points):
    if len(points) < 3:
        return 0.0
    
    points = sorted(points)
    
    lower = []
    for p in points:
        while len(lower) >= 2:
            x1, y1 = lower[-2]
            x2, y2 = lower[-1]
            x3, y3 = p
            val = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
            if val <= 0:
                lower.pop()
            else:
                break
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2:
            x1, y1 = upper[-2]
            x2, y2 = upper[-1]
            x3, y3 = p
            val = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
            if val <= 0:
                upper.pop()
            else:
                break
        upper.append(p)
    
    hull = lower[:-1] + upper[:-1]
    
    if len(hull) < 3:
        return 0.0
    
    area = 0.0
    n = len(hull)
    for i in range(n):
        x1, y1 = hull[i]
        x2, y2 = hull[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)
    
    return abs(area) / 2.0

if __name__ == '__main__':
    points = [(0, 0), (4, 0), (4, 4), (0, 4)]
    result = convex_hull_area(points)
    print(result)