from typing import List, Tuple

def orientation(p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]) -> int:
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else 2

def distance_squared(p: Tuple[int, int], q: Tuple[int, int]) -> int:
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2

class ConvexPolygonAreaCalculator:
    def __init__(self, points: List[Tuple[int, int]]):
        self.points = points
        if len(points) < 3:
            raise ValueError('At least three points are required to form a polygon')
    
    def convex_hull(self) -> List[Tuple[int, int]]:
        start = min(self.points, key=lambda x: (x[0], -x[1]))
        self.points.remove(start)
        sorted_points = sorted(self.points, key=lambda p: (orientation(start, p, (start[0] + 1, start[1])), distance_squared(p, start)))
        hull = [start, sorted_points[0]]
        for i in range(1, len(sorted_points)):
            while len(hull) >= 2 and orientation(hull[-2], hull[-1], sorted_points[i]) != 1:
                hull.pop()
            hull.append(sorted_points[i])
        return hull
    
    def calculate_area(self) -> float:
        hull = self.convex_hull()
        n = len(hull)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += hull[i][0] * hull[j][1]
            area -= hull[j][0] * hull[i][1]
        return abs(area) / 2.0

if __name__ == "__main__":
    sample_points = [(0, 0), (4, 0), (4, 3), (0, 3), (1, 1)]
    calculator = ConvexPolygonAreaCalculator(sample_points)
    print("Convex Hull Points:", calculator.convex_hull())
    print("Area of Convex Polygon:", calculator.calculate_area())