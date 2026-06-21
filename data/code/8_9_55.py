from typing import List, Tuple

class ConvexHull:
    def __init__(self, points: List[Tuple[int, int]]):
        self.points = sorted(set(points))
        if len(self.points) < 3:
            raise ValueError('At least three unique points are required to form a polygon')

    def orientation(self, p: Tuple[int, int], q: Tuple[int, int], r: Tuple[int, int]) -> int:
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        return 1 if val > 0 else 2

    def monotone_chain(self) -> List[Tuple[int, int]]:
        n = len(self.points)
        lower_hull = []
        for p in self.points:
            while len(lower_hull) >= 2 and self.orientation(lower_hull[-2], lower_hull[-1], p) != 1:
                lower_hull.pop()
            lower_hull.append(p)

        upper_hull = []
        for p in reversed(self.points):
            while len(upper_hull) >= 2 and self.orientation(upper_hull[-2], upper_hull[-1], p) != 1:
                upper_hull.pop()
            upper_hull.append(p)

        return lower_hull[:-1] + upper_hull[:-1]

    def area(self) -> float:
        hull = self.monotone_chain()
        n = len(hull)
        if n < 3:
            raise ValueError('The points do not form a valid polygon')
        
        area = 0
        for i in range(n):
            j = (i + 1) % n
            area += hull[i][0] * hull[j][1]
            area -= hull[j][0] * hull[i][1]
        return abs(area) / 2.0

if __name__ == "__main__":
    points = [(0, 0), (4, 0), (4, 3), (0, 3), (1, 1)]
    convex_hull_instance = ConvexHull(points)
    
    print("Convex Hull Points:", convex_hull_instance.monotone_chain())
    print("Area of the Polygon:", convex_hull_instance.area())