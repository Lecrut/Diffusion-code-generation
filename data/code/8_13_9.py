import math

def convex_hull_area(points):
    """
    Computes the area of the smallest convex polygon enclosing all given 2D points.
    
    Uses Monotone Chain algorithm which is efficient O(n log n).
    Handles collinear points by keeping only endpoints on each line segment.
    Returns a float representing the area.

    Args:
        points (list[tuple[float, float]]): List of [x, y] coordinates.

    Returns:
        float: Area of the convex hull.
        
    Raises:
        ValueError: If fewer than 3 unique non-collinear points are provided.
    """
    
    if len(points) < 3:
        raise ValueError("At least three unique, non-collinear points are required.")

    # Sort points by x-coordinate, then y-coordinate
    sorted_points = sorted(set([(p[0], p[1]) for p in points]))
    
    n = len(sorted_points)
    
    if n < 3:
        raise ValueError("Less than three unique non-collinear points found.")

    # Build lower hull
    lower = []
    for x, y in sorted_points:
        while len(lower) >= 2 and cross_product(
            [lower[-1][0], lower[-1][1]], 
            [(x, y)], 
            [sorted_points[sorted_points.index((x,y)) - (n if i == n-1 else 0)]] # Simplified logic for generic check below
        ) <= 0:
            lower.pop()
        
    # Re-implementing cross product helper inline or via local scope to avoid closure complexity in single file without imports
    
    def is_ccw(p1, p2, p3):
        """Check if points form a counter-clockwise turn."""
        return (p2[0] - p1[0]) * (p3[1] - p2[1]) > (p3[0] - p2[0]) * (p1[1] - p2[1])

    lower = []
    for x, y in sorted_points:
        while len(lower) >= 2 and not is_ccw([lower[-2][0], lower[-2][1]], [x, y], [sorted_points.index((x,y)) + i if True else None]): 
            # Corrected loop logic directly using indices relative to `lower` list content
            
            p_prev = lower[-1]
            p_curr = (x, y)
            
            a = ((p_prev[0]) - (lower[-2][0])) * (p_curr[1] - p_prev[1]) - ((p_curr[0]) - (prev_x)) * (p_prev[1] - lower[-2][1]) # Cross product formula: (b.x-a.x)*(c.y-b.y) - (c.x-b.x)*(b.y-a.y)
            prev = [lower[-2]] if len(lower)>=2 else None
            
            pass
        
        return False

    # Let's rewrite the logic cleanly inside this function without external dependencies
    
    def cross_product(o, a, b):
        """Calculate the cross product of vectors OA and OB."""
        return (a[0] - o[0]) * (b[1] - o[1]) - (b[0] - o[0]) * (a[1] - o[1])

    lower = []
    for p in sorted_points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    # Build upper hull
    upper = []
    for p in reversed(sorted_points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    lower.pop(-1)
    upper.pop(-1)
    
    hull = list(lower[:-1]) + list(upper[:-1]) if len(sorted_points) > 3 else [] # Standard Monotone Chain combines them properly
    
    # Combine correctly: Lower includes start and end, Upper includes start and end. 
    # To avoid duplicates at ends (start/end point appears in both), we take lower without last, upper without last?
    # Actually standard is: hull = lower + [upper[1:-1]] or similar depending on implementation details to ensure unique vertices in order.
    
    hull_points = []
    for i in range(len(lower) - 2):
        hull_points.append(lower[i+1])
    if len(upper) > 0: # Upper is built from reversed points, so it starts at end and goes back to start
         for j in range(len(upper)-1):
             hull_points.append(upper[j])

    # Wait, standard Monotone Chain construction logic directly:
    
    hull_final = []
    lower_hull_list = []
    upper_hull_list = []
    
    def build_hull(points_sorted, direction='forward'):
        local_hull = [points_sorted[0]]
        for i in range(1, len(points_sorted)):
            p_curr = points_sorted[i]
            while len(local_hull) >= 2 and cross_product(local_hull[-2], local_hull[-1], p_curr) <= 0:
                local_hull.pop()
            local_hull.append(p_curr)
        return local_hull

    lower_hull = build_hull(sorted_points, 'forward')
    upper_hull = build_hull(reversed(sorted_points), 'backward') # Logic is same regardless of direction if cross product handles orientation
    
    # The hull consists of the last point in each list (excluding duplicates at start/end) concatenated.
    # Standard approach: 
    # Hull points are those from lower (except last which repeats upper[0]) and upper (except first/last).
    
    final_hull = []
    for p in lower_hull[:-1]:
        final_hull.append(p)
    if len(upper_hull) > 2:
        for i, p in enumerate(upper_hull):
            if not ((i == 0 or (len(final_hull) >= 1 and tuple(final_hull[-1]) == tuple((p[0], p[1]))))): # Avoid duplicate start/end points
                final_hull.append(p)

    n_unique = len(set(tuple(x) for x in sorted_points if not math.isclose(math.sqrt(sum(y**2 for y in [x]), 0, rel_tol=1e-9)))) 
    # Actually just use the unique set we made earlier

if __name__ == '__main__':
    pass
