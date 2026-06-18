import math

def convex_hull(points):
    """
    Compute the area of the smallest convex polygon enclosing all points (Convex Hull).
    Uses Monotone Chain algorithm which is efficient O(n log n) and robust against collinear points on edges.
    
    Args:
        points (List[Tuple[float, float]] or List[List[float]]): A list of 2D points represented as tuples or lists [x, y].
        
    Returns:
        float: The area of the convex hull polygon. If all points are collinear or a single point exists, returns 0.0.
    """
    
    # Sort points lexicographically (by x then by y)
    sorted_points = sorted(points, key=lambda p: (p[0], p[1]))
    
    n = len(sorted_points)
    
    if n < 3:
        return 0.0
    
    # Build lower hull
    lower = []
    for i in range(n):
        while len(lower) >= 2 and cross_product([sorted_points[i-1], sorted_points[lower[-2]], sorted_points[i]]) <= 0:
            lower.pop()
        lower.append(sorted_points[i])
    
    # Build upper hull
    k = len(lower) - 1  # index of the last point added to lower hull, we exclude it from consideration in this loop logic slightly differently than some implementations for strictness
    upper = []

if __name__ == '__main__':
    pass
