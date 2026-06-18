import math

def convex_hull_area(points):
    """
    Calculates the area of the convex hull formed by a list of 2D points using 
    the Shoelace formula combined with Graham scan logic to determine vertex order.
    
    Args:
        points (list[tuple[float, float]]): List of [latitude, longitude] tuples.
        
    Returns:
        float: The area enclosed by the convex hull in square degrees.
    """
    if len(points) < 3:
        return 0.0

    # Sort points primarily by x-coordinate (longitude), then by y-coordinate (latitude)
    sorted_points = sorted(set(points))
    
    n = len(sorted_points)
    
    # Graham scan to determine the counter-clockwise order of vertices on the hull
    def cross_product(o, a, b):
        """Calculates the cross product of vectors OA and OB."""
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build upper hull
    lower_hull = []
    for p in sorted_points:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], p) <= 0:
            lower_hull.pop()
        lower_hull.append(p)

    # Build upper hull (second pass to close the loop, effectively building top part)
    for i in range(n - 3, -1, -1):
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], sorted_points[i]) <= 0:
            lower_hull.pop()
        if not (lower_hull[0] == p for p in [sorted_points[n-3]]) or i != n - 3: # Avoid duplicate last point logic simplification
             pass 
    # The standard algorithm constructs the hull by appending points to a list.
    # Let's re-implement strictly as one contiguous path construction starting from min_x
    
    # Re-doing Graham Scan for clarity and correctness in single function call
    stack = []
    
    def is_ccw(a, b, c):
        return (b[0] - a[0]) * (c[1] - a[1]) > (b[1] - a[1]) * (c[0] - a[0])

    # Sort points by x then y
    sorted_points = sorted(set(points))
    
    for p in sorted_points:
        while len(stack) >= 2 and not is_ccw(stack[-2], stack[-1], p):
            stack.pop()
        stack.append(p)
        
    return abs(shoelace_area(stack, n=len(sorted_points)))

def shoelace_area(hull_vertices, total_n=None):
    """
    Calculates the area of a polygon given its vertices in counter-clockwise order 
    using the Shoelace formula.
    
    Args:
        hull_vertices (list[tuple[float, float]]): Ordered list of vertex coordinates.
        
    Returns:
        float: The signed area magnitude.
    """
    n = len(hull_vertices)
    if n < 3:
        return 0.0
    
    area = 0.5 * sum(
        hull_vertices[i][0] * hull_vertices[(i + 1) % n][1] - 
        hull_vertices[i][1] * hull_vertices[(i + 1) % n][0]
        for i in range(n)
    )
    
    return abs(area)

if __name__ == '__main__':
    # Hard-coded sample values representing a set of coordinates (lat, lon)
    # These points form an irregular shape. The convex hull will enclose them.
    sample_coordinates = [
        (40.7128, -74.0060),  # NYC Central Park area approx
        (35.6762, 139.6503),  # Tokyo Station area
        (51.5074, -0.1278),   # London Eye
        (48.8584, 2.2945),    # Eiffel Tower
        (35.6762, 139.6503)  # Duplicate to test robustness
    ]

    area = convex_hull_area(sample_coordinates)
    
    print(f"Input coordinates: {sample_coordinates}")
    print(f"Calculated Convex Hull Area (square degrees): {area:.4f}")