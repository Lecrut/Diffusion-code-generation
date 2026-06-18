import math

def convex_hull_area(points):
    """
    Computes the area of the smallest convex polygon enclosing all given 2D points.
    Uses the Monotone Chain algorithm which is efficient (O(n log n)).
    
    Args:
        points (list[tuple]): List of (x, y) tuples representing 2D points.
        
    Returns:
        float: The area of the convex hull polygon.
    """
    if len(points) < 3:
        return 0.0

    # Sort points primarily by x-coordinate, secondarily by y-coordinate
    sorted_points = sorted(set(points))
    
    # Build lower and upper halves of the convex hull
    def cross(o, a, b):
        """Calculate the cross product of vectors OA and OB."""
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    lower = []
    for p in sorted_points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(sorted_points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate the two halves; remove last point of each half because it's repeated at start of other
    hull = lower[:-1] + upper[:-1]
    
    if len(hull) < 3:
        return 0.0
    
    # Calculate area using the Shoelace formula (Green's theorem)
    area = 0.5 * abs(sum((hull[i][0] + hull[(i+1)%len(hull)]) * (hull[i+1][1] - hull[i-1][1]) for i in range(len(hull)))) / len(hull)

    return area

if __name__ == '__main__':
    # Hard-coded sample values: a set of points forming an irregular shape
    sample_points = [
        (0, 0),
        (4, 0),
        (5, 2),
        (3, 4),
        (1, 3)
    ]

    area_result = convex_hull_area(sample_points)
    
    print(f"Area of the smallest convex polygon enclosing the points: {area_result}")