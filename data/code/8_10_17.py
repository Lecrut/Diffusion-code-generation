import math

def convex_hull_area(coordinates):
    """
    Calculates the area of the convex hull formed by a list of 2D coordinates (latitude, longitude).
    
    Uses Monotone Chain algorithm to find vertices in counter-clockwise order and then applies 
    the Shoelace formula for area calculation. This approach is O(n log n) due to sorting, 
    which is optimal for this problem given no pre-sorted input guarantee.

    Args:
        coordinates (list[tuple[float]]): List of [lat, lon] tuples representing points on a plane.
        
    Returns:
        float: The area enclosed by the convex hull in square degrees.
    
    Note: 
        This calculates geometric area based purely on coordinate values as if they were Cartesian 
        coordinates (x=lon, y=lat). For real-world map areas requiring projection corrections, 
        additional geospatial libraries would be necessary. However, per task constraints focusing 
        on the Shoelace formula implementation via convex hull logic:
    """

    # Sort points lexicographically by x-coordinate then y-coordinate (longitude then latitude)
    sorted_points = sorted(coordinates, key=lambda p: (p[1], p[0]))

    if len(sorted_points) < 3:
        return 0.0

    def cross_product(o, a, b):
        """Calculates the cross product of vectors OA and OB."""
        return (a[1] - o[1]) * (b[0] - a[0]) - (a[0] - o[0]) * (b[1] - a[1])

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

    # Concatenate lower and upper to get full hull, removing duplicate last point of each half
    if len(lower) > 1 or len(upper) > 1:
        return cross_product_area([lower[:-1] + upper[:-1]])
    
    return 0.0

def cross_product_area(hull_points):
    """
    Applies the Shoelace formula to calculate area from ordered polygon vertices.

    Args:
        hull_points (list[tuple[float]]): Ordered list of [lat, lon] tuples forming a closed loop.

    Returns:
        float: Area calculated as 0.5 * |sum(x_i*y_{i+1} - x_{i+1}*y_i)|
    
    Note: 
        The Shoelace formula computes signed area; absolute value ensures positive result.
    """
    n = len(hull_points)

    if n < 3:
        return 0.0
    
    # Ensure we have a closed loop by appending the first point at the end for calculation purposes, 
    # though mathematically redundant in sum since terms cancel out correctly with modulo indexing logic below.
    
    area_sum = 0.0

    for i in range(n):
        x1, y1 = hull_points[i]
        x2, y2 = hull_points[(i + 1) % n]
        
        # Shoelace term: x_i * y_{i+1} - x_{i+1} * y_i
        area_sum += (x1 * y2 - x2 * y1)

    return abs(area_sum) / 2.0

if __name__ == '__main__':
    # Hard-coded sample values representing a simple polygon: 
    # A square rotated slightly for demonstration purposes.
    # Coordinates are [latitude, longitude] as per task requirement.
    
    sample_points = [
        (45.1234, -76.0),   # Point 1
        (45.5678, -75.9) ,  # Point 2
        (45.2345, -75.5) ,  # Point 3
        (44.8901, -76.2)   # Point 4
    ]

    area = convex_hull_area(sample_points)
    
    print(f"Total Area of Convex Hull: {area:.6f} square degrees")