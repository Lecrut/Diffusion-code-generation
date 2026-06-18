import math

def convex_hull_area(points):
    """
    Computes the area of the smallest convex polygon enclosing a given set of 2D points.
    
    Uses the Monotone Chain algorithm which is O(n log n) efficient and robust against 
    collinear point handling (though it includes them in boundary, they don't affect area calculation).
    
    Args:
        points (list[tuple[float, float]]): List of 2D points as tuples. Duplicate or redundant points are handled gracefully.
        
    Returns:
        float: The area of the convex hull polygon.
    """
    # Remove duplicates and sort by x-coordinate, then y-coordinate
    unique_points = sorted(set(points))
    
    if len(unique_points) < 3:
        return 0.0

    def cross(o, a, b):
        """Compute the cross product of vectors OA and OB."""
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull
    lower = []
    for p in unique_points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(unique_points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate lower and upper to get full hull, removing the last point of each half 
    # because it's repeated at the start/end (e.g., first point is also last in circular buffer logic if needed, but here we just join).
    # Actually Monotone chain usually constructs: lower + reversed(lower[:-1]) or similar.
    # Standard construction: hull = lower[:-1] + upper[:-1] to avoid duplication of start/end points.
    
    hull = lower[:-1] + upper[:-1]

    if len(hull) < 3:
        return 0.0
    
    # Compute area using the shoelace formula
    n = len(hull)

if __name__ == '__main__':
    pass
