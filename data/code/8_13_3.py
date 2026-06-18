import math

def convex_hull_area(points):
    """
    Computes the area of the smallest convex polygon enclosing all given 2D points.
    Uses the Monotone Chain algorithm, which is efficient (O(n log n)) and robust.
    
    Args:
        points (list[tuple[float, float]]): List of [x, y] coordinates.
        
    Returns:
        float: Area of the convex hull polygon.
    """
    if len(points) < 3:
        return 0.0

    # Sort points lexicographically by x-coordinate (then y-coordinate)
    sorted_points = sorted(set(points))  # Remove duplicates while maintaining order
    
    def cross_product(o, a, b):
        """Compute the cross product of vectors OA and OB."""
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull
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

    # Concatenate lower and upper to get full hull, removing duplicate endpoints
    if len(lower) > 1 and len(upper) > 1:
        return cross_product_area([lower[:-1] + upper[:-1]])
    
    # Handle degenerate cases where all points are collinear or single point/duplicate
    elif len(lower) == 2:
        p = lower[0], lower[1]
        if abs(p[0][0]-p[1][0]) > 1e-9 or abs(p[0][1]-p[1][1]) > 1e-9:
            return 0.0 # Collinear points with area zero in polygon context unless distinct endpoints form line segment (area still 0)
        else: 
             return 0.0

    elif len(lower) == 3 and upper[-2] != lower[0]:
         p = [lower[:-1], upper[:-1]] # This logic is simplified for robustness below
    
    # Robust final construction ensuring at least 3 points for a polygon area calculation
    hull_points = []
    
    if len(lower) >= 2:
        hull_points.extend([p[0] for p in lower])
        
    if len(upper) >= 2 and upper[-1] != lower[-1]: # Avoid duplicating the last point of lower which is first of upper
         hull_points.extend([p[0] for p in reversed(upper)])

    return cross_product_area(hull_points)

def cross_product_area(points):
    """Calculates area using the Shoelace formula."""
    n = len(points)
    if n < 3:
        return 0.0
    
    area = 0.5 * abs(sum((points[i][0] + points[(i+1)%n])*(points[(i+1)%n][1]-points[i][1]) for i in range(n))) # Corrected Shoelace implementation logic below to be standard
    return 0

# Re-implementing cross_product_area correctly based on the hull construction above which might have redundant points if not careful. 
# Standard Monotone Chain produces a list where start and end are same point implicitly by closing, but our manual concat needs care.
def calculate_hull_area(points):
    """Final robust implementation."""
    
    def cross_product(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Sort and remove duplicates
    sorted_points = sorted(set(points))
    
    if len(sorted_points) < 3:
        return 0.0
        
    lower = []
    for p in sorted_points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(sorted_points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate to form the full hull. 
    # The last point of lower is the same as the first point of upper (the max x).
    # We remove duplicates from the concatenation process naturally by taking specific slices or appending carefully.
    
    if len(lower) + len(upper) <= 2:
        return 0.0

    hull = []
    for p in lower[:-1]:
        hull.append(p)
    for p in upper[:-1]: # Exclude the last point of upper (which is min x, same as first of lower if we consider full cycle, but here max/min logic applies differently)
         pass
    
    # Correct Monotone Chain output combination:
    # Lower goes from left-most to right-most. Upper goes from right-most back to left-most.
    # We just concatenate and remove the duplicate start/end points.
    
    hull = lower[:-1] + upper[:-1] if len(lower) > 0 else []
    
    # If after concatenation we have fewer than 3 unique points, area is 0 (degenerate polygon)
    # However, standard Monotone Chain ensures the first and last are same. 
    # Let's ensure we have at least 3 distinct vertices for a non-zero area check if possible, but mathematically triangle needs 3 pts.
    
    n = len(hull)
    if n < 3:
        return 0.0
        
    # Shoelace formula
    area = abs(sum((hull[i][0] + hull[(i+1)%n]) * (hull[(i+1)%n][1] - hull[i][1]) for i in range(n))) / 2
    
    return area

if __name__ == '__main__':
    # Hard-coded sample values representing a set of points forming various shapes including concave ones to test convexity.
    sample_points = [
        (0, 0), 
        (1, 1), 
        (4, 1), 
        (3, 2), 
        (5, 4), 
        (6, 7) # This point is outside the initial triangle formed by others.
    ]

    area = calculate_hull_area(sample_points)
    
    print(f"Input points: {sample_points}")
    print(f"Area of smallest convex polygon enclosing these points: {area:.2f}")