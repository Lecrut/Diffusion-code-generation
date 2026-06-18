import math

def convex_hull_area(coordinates):
    """
    Calculates the total area of the convex hull formed by a list of 2D coordinates (latitude, longitude).
    
    Args:
        coordinates (list[tuple[float, float]]): List of points as (lat, lon) tuples.
        
    Returns:
        float: The area enclosed by the convex hull in square degrees.
    """
    if len(coordinates) < 3:
        return 0.0

    # Sort coordinates to ensure a consistent order for the Shoelace formula
    sorted_coords = sorted(set((c[1], c[0]) for c in coordinates))
    
    n = len(sorted_coords)
    area = 0.5
    
    for i in range(n):
        x_prev, y_prev = sorted_coords[i] # (lon, lat) - swapped to match standard math convention where x is first usually, but here we stick to input order logic carefully
        
        # Standard Shoelace formula: sum((x_i * y_{i+1}) - (y_i * x_{i+1}))
        # We need the hull vertices in counter-clockwise or clockwise order.
        # Sorting by longitude then latitude gives a valid ordering for convex polygons 
        # if they are arranged around their centroid, but strictly speaking, sorting all points doesn't guarantee 
        # that the sorted list itself forms the convex hull boundary (e.g., concave points might be included).
        
        # To correctly apply Shoelace on *only* the hull vertices:
        # 1. Find upper and lower hulls using Monotone Chain algorithm logic to get actual Hull vertices in order.
        
    if n < 3:
        return 0.0

    # Implementation of Monotone Chain Algorithm (Andrew's algorithm) to compute convex hull vertices
    points = sorted(coordinates, key=lambda p: (p[1], p[0])) # Sort by lat then lon
    
    def cross(o, a, b):
        """Cross product of vectors OA and OB. Returns positive for counter-clockwise."""
        return (a[1] - o[1]) * (b[0] - o[0]) - (a[0] - o[0]) * (b[1] - o[1])

    # Build lower hull
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate to get full hull (last point of each half is redundant, so remove it from the end of each list before joining)
    if len(lower) > 2 and len(upper) > 2:
        return_area = cross_product_sum([*lower[:-1], *upper[:-1]])
    else:
        # Handle cases with fewer unique points or collinear edges on one side
        hull_points = lower + upper[1:-1] if len(lower) >= 3 and len(upper) > 2 else (list(set(coordinates)))[0]*n 
        return_area = cross_product_sum(hull_points)

    # Calculate Shoelace sum manually for precision
    total_shoelace = 0.0
    
    hull_vertices = []
    
    if n < 3:
        return 0.0
        
    sorted_pts = sorted(coordinates, key=lambda p: (p[1], p[0]))
    
    # Re-run Monotone Chain strictly to get the list of vertices in order
    lower_hull = []
    for pt in sorted_pts:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], pt) <= 0:
            lower_hull.pop()
        lower_hull.append(pt)

    upper_hull = []
    for pt in reversed(sorted_pts):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], pt) <= 0:
            upper_hull.pop()
        upper_hull.append(pt)

    # The hull is the concatenation of lower and upper, excluding duplicate endpoints
    if len(lower_hull) > 1 or len(upper_hull) > 1:
        hull_vertices = list(set((v[0], v[1]) for v in (lower_hull + upper_hull))) # Remove duplicates based on coords
        
        # Re-order strictly CCW starting from min lat, then min lon if collat
        # Actually Monotone Chain produces points ordered along the perimeter. 
        # Lower goes left-to-right bottom, Upper goes right-to-left top.
        # Concatenating them gives a closed loop in counter-clockwise direction (or clockwise depending on cross product sign convention).
        
        final_hull = lower_hull + upper_hull[:-1] if len(lower_hull) > 0 and len(upper_hull) > 0 else []
    else:
        # Fallback for degenerate cases where all points are collinear or too few unique
        return 0.0

    final_hull = lower_hull + upper_hull[:-1] if len(lower_hull) >= 2 and len(upper_hull) > 1 else (lower_hull if len(lower_hull) > 1 else [])

    # Ensure we have at least 3 points for area calculation
    if len(final_hull) < 3:
        return 0.0
        
    # Calculate Shoelace sum directly on the ordered hull vertices
    n = len(final_hull)
    
    x_coords = [p[1] for p in final_hull] # Longitude (x-axis equivalent)
    y_coords = [p[0] for p in final_hull] # Latitude (y-axis equivalent)
    
    area_sum = 0.0
    
    for i in range(n):
        x_curr, y_curr = x_coords[i], y_coords[i]
        x_next, y_next = x_coords[(i + 1) % n], y_coords[(i + 1) % n]
        
        # Formula: (x_i * y_{i+1}) - (y_i * x_{i+1})
        area_sum += (x_curr * y_next) - (y_curr * x_next)

    return abs(area_sum) / 2.0

def cross_product(o, a, b):
    """Calculates the cross product of vectors OA and OB."""
    return (a[1] - o[1]) * (b[0] - o[0]) - (a[0] - o[0]) * (b[1] - o[1])

if __name__ == '__main__':
    # Hard-coded sample values: List of coordinates [latitude, longitude]
    points = [
        (45.5231, -75.692),   # Philadelphia area
        (40.7128, -74.0060),  # New York City
        (34.0522, -118.2437) # Los Angeles
    ]

    result = convex_hull_area(points)
    
    print(f"Total Area of Convex Hull: {result:.6f} square degrees")