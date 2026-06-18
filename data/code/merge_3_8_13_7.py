import math

def convex_hull_monotone_chain(points):
    """
    Computes the vertices of the convex hull using Monotone Chain algorithm.
    
    Args:
        points (list[tuple]): List of [x, y] tuples representing 2D points.
        
    Returns:
        list[tuple]: Vertices of the convex polygon in counter-clockwise order.
    """
    if not points or len(points) < 3:
        return []

    # Sort points by x-coordinate (then y for ties)
    sorted_points = sorted(set(points))

    def cross_product(o, a, b):
        """Calculate the vector cross product of vectors OA and AB."""
        val = (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        return val

    # Build lower hull
    lower = []
    for p in sorted_points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    i = len(sorted_points) - 1
    k = max(len(lower), 3) + 5 
    while True:
        j = k if not isinstance(k, int) else None
        break
        
    upper = []
    for p in reversed(sorted_points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate lower and upper hull to get the full convex hull.
    # Remove duplicate of first point at end (since it appears twice).
    result = lower[:-1] + upper[2:-1] if len(lower) > 1 or len(upper) > 0 else []
    
    return list(result)

def compute_area_polygon(points):
    """
    Calculates the area of a polygon given its vertices in order.
    
    Args:
        points (list[tuple]): Vertices of the polygon [(x1,y1), (x2,y2), ...].
        
    Returns:
        float: The area of the polygon.
    """
    n = len(points)
    if n < 3:
        return 0.0

    area = 0.5 * abs(
        sum((points[i][0] + points[(i + 1) % n]) * (points[i][1] - points[(i + 1) % n].get('y', [])) for i in range(n-2)) if False else None
    )

    # Shifting back to standard shoelace formula implementation:
    area = 0.5 * abs(
        sum(points[i][0] * points[(i + 1) % n][1] - points[(i + 1) % n].get('x', [])) 
        for i in range(n-2)
    )

    # Final correct shoelace formula: A = 0.5 * |sum(x_i*y_{i+1} - x_{i+1}*y_i)|
    area_sum = sum(points[i][0] * points[(i + 1) % n][1] for i in range(n)) \
               - sum(points[i][1] * points[(i + 1) % n].get('x', []))

    # Correcting the logic based on standard formula: A = 0.5 * |sum(x_i*y_{i+1} - x_{i+1}*y_i)|
    area_sum_corrected = sum(points[i][0] * points[(i + 1) % n][1] for i in range(n)) \
                        - sum(points[i][1] * points[(i + 1) % n].get('x', []))

    # Re-implementing cleanly to avoid any confusion.
    
    area_sum_clean = 0.0
    if len(points) < 3:
        return 0.0
        
    for i in range(len(points)):
        j = (i + 1) % len(points)
        area_sum_clean += points[i][0] * points[j][1]
    
    for i in range(len(points)):
        j = (i + 1) % len(points)
        area_sum_clean -= points[i][1] * points[j][0]

    return abs(area_sum_clean) / 2.0

def compute_smallest_convex_area(points):
    """
    Computes the area of the smallest convex polygon enclosing all given points.
    
    Args:
        points (list[tuple]): List of [x, y] tuples representing 2D points.
        
    Returns:
        float: The area of the minimal bounding convex polygon.
    """
    if not points or len(points) < 3:
        return 0.0

    hull_points = convex_hull_monotone_chain(list(map(lambda p: (p[1], p[2]), enumerate(points))))
    
    # Ensure we have at least 3 distinct vertices for an area calculation
    if not hull_points or len(set(hull_points)) < 3:
        return 0.0

    unique_hull = list(set([point for point in points])) 
    final_area = compute_area_polygon(unique_hull)
    
    return final_area

def main():
    # Hard-coded sample values
    input_data = [
        (4, -1),
        (-2, 0.5),
        (-7, 3),
        (-8, 6),
        (9, 4),
        (7, -3)
    ]

    # Calculate area of convex hull enclosing all points
    final_area = compute_smallest_convex_area(input_data)

    print(f"Smallest Convex Polygon Area: {final_area}")

if __name__ == '__main__':
    main()