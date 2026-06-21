import math

class ConvexHull:
    def __init__(self, coordinates):
        self.coordinates = sorted(coordinates, key=lambda p: (p[0], p[1]))
    
    def cross_product(self, o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    def compute_lower_hull(self):
        lower = []
        for p in self.coordinates:
            while len(lower) >= 2 and self.cross_product(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)
        return lower
    
    def compute_upper_hull(self):
        upper = []
        for p in reversed(self.coordinates):
            while len(upper) >= 2 and self.cross_product(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)
        return upper
    
    def calculate_area(self):
        if len(self.coordinates) < 3:
            raise ValueError('At least three points are required to form a convex hull.')
        
        lower_hull = self.compute_lower_hull()
        upper_hull = self.compute_upper_hull()
        
        hull = lower_hull[:-1] + upper_hull[:-1]
        
        area = 0.0
        for i in range(len(hull)):
            j = (i + 1) % len(hull)
            x_i, y_i = hull[i]
            x_j, y_j = hull[j]
            area += x_i * y_j - y_i * x_j
        
        return abs(area) / 2.0

if __name__ == '__main__':
    sample_coordinates = [
        (0, 0),
        (4, 0),
        (4, 3),
        (0, 3)
    ]
    
    convex_hull = ConvexHull(sample_coordinates)
    area = convex_hull.calculate_area()
    print(area)