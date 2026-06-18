import math
from typing import List, Tuple

def convex_hull_area(points: List[Tuple[float, float]]) -> float:
    """
    Calculates the area of the convex hull formed by a list of 2D points using 
    the Shoelace formula. Points are assumed to be (latitude, longitude). 
    
    Optimized implementation with O(n log n) complexity via sorted coordinates 
    for sorting and linear scan for triangulation logic if needed, but here 
    we use Graham Scan approach implicitly by sorting first then applying monotone chain algorithm's area calculation step which is efficient.
    
    However, since the task specifies Shoelace specifically on the convex hull vertices:
    1. Compute actual convex hull vertices (Monotone Chain algorithm - O(n log n))
    2. Apply Shoelace formula to those vertices
    
    This ensures we only sum over boundary points for maximum accuracy and performance 
    given large datasets, rather than using all potentially interior points in a naive shoelace.
    
    Args:
        points: List of (lat, lon) tuples
        
    Returns:
        Area as a float
    """
    if not points or len(points) < 3:
        return 0.0
    
    # Sort points by x-coordinate then y-coordinate for Monotone Chain
    sorted_points = sorted(set(points))
    
    n = len(sorted_points)
    
    def cross(o, a, b):
        """Cross product of vectors OA and OB."""
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    # Build lower hull
    lower = []
    for p in sorted_points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
        
    # Build upper hull
    upper = []
    for p in reversed(sorted_points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    # Concatenate lower and upper to get full hull, removing last two points 
    # as they are repeated from start/end of respective chains for Monotone Chain standard form
    if len(lower) > 1:
        h = [p[0] for p in lower[:-1]] + [p[0] for p in upper[:-2]] + [lower[-1][0], lower[0][0]] # Keep start and end unique
        
        # Actually reconstruct proper vertex list properly handling duplicates at corners
    
    hull_vertices = []
    
    if n >= 3:
        # Re-implement Monotone Chain to get correct vertices without duplication errors
        k = len(sorted_points) + 1 - (k > 0 and sorted_points[2] != sorted_points[-2]) * 1
        
        lower_hull = []
        for p in sorted_points:
            while len(lower_hull) >= 2 and cross(lower_hull[-2], lower_hull[-1], p) <= 0:
                lower_hull.pop()
            lower_hull.append(p)
        
        upper_hull = []
        for p in reversed(sorted_points):
            while len(upper_hull) >= 2 and cross(upper_hull[-2], upper_hull[-1], p) <= 0:
                upper_hull.pop()
            upper_hull.append(p)
        
        # Concatenate lower and upper, excluding the last point of each because 
        # it's repeated as the first point in the other chain (e.g. start/end overlap)
        if len(lower_hull) <= 1 or len(upper_hull) <= 1:
            return 0.0
            
        hull_vertices = list(lower_hull[:-1]) + [lower_hull[-1]] # Add last point of lower back to close loop implicitly handled by upper structure
        
    else:
        if n == 2:
            area = abs((sorted_points[0][0] * sorted_points[1][1] - sorted_points[0][1] * sorted_points[1][0])) / 2.0
            return area
            
        return 0.0

    # Apply Shoelace formula to the convex hull vertices for final area calculation
    
    if len(hull_vertices) < 3:
        return 0.0
        
    x_coords = [p[0] for p in hull_vertices]
    y_coords = [p[1] for p in hull_vertices]
    
    area_sum_1 = sum(x[i+1]%len(hull_vertices)*y[i] if i<len(y)-1 else x_i*y_next) 
    # Correct Shoelace implementation inline

if __name__ == '__main__':
    pass
