import math

def convex_hull_area(coordinates):
    """
    Calculates the area of the convex hull formed by a list of 2D coordinates (latitude, longitude).
    
    Uses Monotone Chain algorithm to find vertices in counter-clockwise order and then applies 
    the Shoelace formula for area calculation. This approach is O(n log n) which is optimal 
    for general point sets compared to naive sorting or other geometric algorithms.

    Args:
        coordinates (list[tuple[float, float]]): List of [lat, lon] tuples representing points on Earth's surface.
    
    Returns:
        float: The area in square degrees of the convex hull polygon.
    
    Note: 
        This calculates planar area based on projected latitude/longitude values. For high-precision 
        geodetic calculations involving large areas or specific projections, a proper map projection library 
        (like pyproj) would be required to convert coordinates to Cartesian space first. However, this script 
        adheres strictly to the request of using coordinate pairs directly with the Shoelace formula logic.
    """
    
    if not coordinates:
        return 0.0
    
    n = len(coordinates)
    
    # Sort points lexicographically by x-coordinate (latitude), then y-coordinate (longitude).
    sorted_points = sorted(coordinates, key=lambda p: (p[0], p[1]))
    
    # Build lower hull
    stack_lower = []
    for point in sorted_points:
        while len(stack_lower) >= 2 and cross_product(
            [stack_lower[-2][0], stack_lower[-2][1]], 
            [stack_lower[-1][0], stack_lower[-1][1]], 
            [point[0], point[1]]
        ) <= 0:
            stack_lower.pop()
        stack_lower.append(point)
    
    # Build upper hull
    stack_upper = []
    for i in range(n - 1, -1, -1):
        while len(stack_upper) >= 2 and cross_product(
            [stack_upper[-2][0], stack_upper[-2][1]], 
            [stack_upper[-1][0], stack_upper[-1][1]], 
            [sorted_points[i][0], sorted_points[i][1]]
        ) <= 0:
            stack_upper.pop()
        stack_upper.append(sorted_points[i])
    
    # Concatenate lower and upper hulls. Remove the last point of each list because it's repeated at the start of the other.
    if len(stack_lower) > 2 or len(stack_upper) > 2:
        return _shoelace_area(list(set((p[0], p[1]) for p in stack_lower + stack_upper)))
    
    # Handle degenerate cases where all points are collinear (area should be 0) 
    # or only one/two unique points exist. The set logic above handles duplicates, but if the hull has < 3 vertices:
    return _shoelace_area(list(set((p[0], p[1]) for p in stack_lower + stack_upper)))

def cross_product(o, a, b):
    """Calculates the signed area of triangle OAB to determine convexity."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def _shoelace_area(points):
    """
    Applies the Shoelace formula to calculate polygon area.
    
    Args:
        points (list[tuple[float, float]]): Vertices of the polygon in order.
        
    Returns:
        float: Area calculated as 0.5 * |sum(x_i*y_{i+1} - x_{i+1}*y_i)|
    """
    
    if len(points) < 3:
        return 0.0
    
    area = 0.0
    n = len(points)
    
    for i in range(n):
        j = (i + 1) % n
        x, y = points[i]
        xp, yp = points[j]
        
        # Shoelace term: x_i * y_{i+1} - x_{i+1} * y_i
        area += x * yp - xp * y
    
    return abs(area) / 2.0

if __name__ == '__main__':
    # Hard-coded sample values representing a simple polygon (e.g., a triangle near the equator).
    # Coordinates: [lat, lon]
    sample_points = [
        (45.0, -73.0),  # New York City approx
        (42.0, -81.0),  # Cleveland area approx
        (49.0, -67.0)   # Montreal area approx
    ]

    result_area = convex_hull_area(sample_points)
    
    print(f"Input Points: {sample_points}")
    print(f"Calculated Convex Hull Area: {result_area:.10f} square degrees")