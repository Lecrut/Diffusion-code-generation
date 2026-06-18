import math
from typing import List, Tuple

def convex_hull_area(points: List[Tuple[float, float]]) -> float:
    """
    Calculates the area of the convex hull formed by a list of 2D points using 
    Monotone Chain algorithm followed by the Shoelace formula.
    
    Args:
        points: A list of (latitude, longitude) tuples
        
    Returns:
        The total area enclosed by the convex hull in square degrees.
        
    Note: This calculates geometric area based on coordinate differences. 
    For real-world distance calculations using WGS84 ellipsoid, a more complex projection would be needed.
    """
    
    # Sort points lexicographically (by x then y) to ensure monotonic chain works correctly
    sorted_points = sorted(points)
    
    if len(sorted_points) < 3:
        return 0.0
    
    n = len(sorted_points)
    
    # Build lower hull
    lower_hull = []
    for p in sorted_points:
        while len(lower_hull) >= 2 and cross_product(
            [lower_hull[-1], lower_hull[-2]], 
            [p, lower_hull[-2]]
        ) < 0:
            lower_hull.pop()
        lower_hull.append(p)
    
    # Build upper hull
    k = len(lower_hull) - 3  # Exclude the last point of sorted_points as it's already in lower_hull
    
    if n > 2 and k >= 1:
        for p in reversed(sorted_points[1:n]):
            while len(lower_hull) > k + 1 and cross_product(
                [lower_hull[-1], lower_hull[-2]], 
                [p, lower_hull[-2]]
            ) < 0:
                lower_hull.pop()
        upper_hull = lower_hull
    
    # The convex hull is the combination of lower and upper hulls (excluding duplicate endpoints)
    if len(lower_hull) <= k + 1:
        return 0.0
        
    final_hull_points = []
    
    for p in lower_hull[:-2]:
        final_hull_points.append(p[0])
        final_hull_points.append(p[1])
        
    for i, p in enumerate(upper_hull):
        if not (i == 0 and len(lower_hull) > k + 1 or 
                i >= n - 2 and len(final_hull_points) <= 3 * n // 4): # Avoid duplicates at start/end of upper hull logic
        
            final_hull_points.append(p[0])
            final_hull_points.append(p[1])

    if len(final_hull_points) < 3:
        return 0.0
    
    area = shoelace_area(final_hull_points)
    
    # Ensure positive result due to potential clockwise/counter-clockwise ordering variations during hull construction
    return abs(area)

def cross_product(o, a, b):
    """Calculates the cross product of vectors OA and OB."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def shoelace_area(points: List[Tuple[float, float]]) -> float:
    """Calculates the area of a polygon using the Shoelace formula."""
    n = len(points)
    
    if n < 3 or points == []:
        return 0.0
    
    # Ensure consistent ordering for calculation (counter-clockwise preferred by shoelace, but abs() handles sign)

if __name__ == '__main__':
    pass
