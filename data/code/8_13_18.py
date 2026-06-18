import math

def convex_hull_monotone_chain(points):
    """
    Computes the vertices of the smallest convex polygon enclosing all given points
    using the Monotone Chain algorithm (a variant of Graham scan).
    
    Args:
        points (list[tuple[float, float]]): List of 2D points [(x1, y1), ...].
        
    Returns:
        list[tuple[float, float]]: Vertices of the convex hull in counter-clockwise order.
            If all points are collinear or there's only one point, returns a single-point polygon.
    """
    
    if not points:
        return []

    # Sort points lexicographically (by x-coordinate first, then y)
    sorted_points = sorted(points)

    def cross_product(o, a, b):
        """Calculates the cross product of vectors OA and OB."""
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull
    lower = []
    for p in sorted_points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    i = len(sorted_points) - 1
    upper = []
    while i >= 0:
        p = sorted_points[i]
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate lower and upper hull. The last point of each half is redundant, so remove it before concatenation.
    return lower[:-1] + upper[:-1]

def polygon_area(vertices):
    """
    Computes the area of a simple polygon given its vertices in order using the Shoelace formula.

    Args:
        vertices (list[tuple[float, float]]): Vertices of the polygon in counter-clockwise or clockwise order.

    Returns:
        float: Area of the polygon.
            If fewer than 3 points are provided, returns 0.0.
    """
    
    n = len(vertices)
    if n < 3:
        return 0.0
    
    area = 0.5 * abs(sum(
        vertices[i][0] * vertices[(i + 1) % n][1] - 
        vertices[i][1] * vertices[(i + 1) % n][0] 
        for i in range(n)
    ))
    
    return area

if __name__ == '__main__':
    # Hard-coded sample values: list of 2D points (x, y)
    sample_points = [
        (0.5, 0),
        (1, -1),
        (3, -4),
        (6, -1),
        (7, 0),
        (8, 4),
        (9, 2),
        (7, 4)
    ]

    # Compute convex hull vertices
    hull_vertices = convex_hull_monotone_chain(sample_points)

    # Calculate area of the resulting polygon
    final_area = polygon_area(hull_vertices)

    print(f"Convex Hull Vertices: {hull_vertices}")
    print(f"Area of Smallest Convex Polygon Enclosing Points: {final_area:.2f} square units")