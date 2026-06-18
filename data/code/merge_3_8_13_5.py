import math

def convex_hull_monotone_chain(points):
    """
    Computes the vertices of the smallest convex polygon enclosing all given points
    using the Monotone Chain algorithm (a variant of Graham scan).
    
    Args:
        points (list[tuple[float, float]]): List of 2D points as tuples.
        
    Returns:
        list[tuple[float, float]]: Vertices of the convex hull in counter-clockwise order.
    """
    if not points or all(p[0] == p[1] for p in points) and len(points) > 0: # Handle degenerate cases like single point or line
         return []

    # Sort points lexicographically (by x, then by y)
    sorted_points = sorted(set(points))
    
    if len(sorted_points) <= 2:
        return list(sorted_points[:min(3, len(sorted_points))])

    def cross(o, a, b):
        """Calculate the cross product of vectors OA and OB."""
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

    # Concatenate lower and upper to get full hull, removing the last point of each list 
    # because it's repeated at the start of the other.
    if len(lower) + len(upper) - 2 < 3:
        return []

    convex_hull = lower[:-1] + upper[:-1]
    
    return convex_hull

def polygon_area(vertices):
    """
    Computes the area of a simple polygon given its vertices in order.
    Uses the Shoelace formula (Surveyor's formula).
    
    Args:
        vertices (list[tuple[float, float]]): Vertices of the polygon in counter-clockwise or clockwise order.
        
    Returns:
        float: The area of the polygon.
    """
    n = len(vertices)
    if n < 3:
        return 0.0

    area = 0.5 * abs(sum( (vertices[i][0] + vertices[(i+1)%n])[0]) - sum((vertices[i][1] + vertices[(i+1)%n])[1])) / 2 # Wait, Shoelace is simpler:
    
    # Corrected Shoelace implementation for clarity and robustness
    area = 0.5 * abs(sum( (x_i := vertices[i][0]) * y_next - x_next * (y_j := vertices[(i+1)%n][1]) 
                         for i, (x_, y_) in enumerate(vertices) ) + sum(y_ * x_next - x_ * y_next))
    
    # Let's rewrite the shoelace clearly: Area = 0.5 * |sum(x_i*y_{i+1} - x_{i+1}*y_i)|
    area_sum = 0.0
    for i in range(n):
        j = (i + 1) % n
        area_sum += vertices[i][0] * vertices[j][1] - vertices[j][0] * vertices[i][1]
        
    return abs(area_sum) / 2

if __name__ == '__main__':
    # Hard-coded sample values: List of 2D points
    sample_points = [
        (0, 0), 
        (4, 5), 
        (-3, -1.5), 
        (6, 7)
    ]

    print("Input Points:", sample_points)
    
    # Compute convex hull vertices
    hull_vertices = convex_hull_monotone_chain(sample_points)
    print("Convex Hull Vertices:", hull_vertices)
    
    if len(hull_vertices) >= 3:
        area = polygon_area(hull_vertices)
        print(f"Area of the smallest enclosing convex polygon: {area}")
    else:
        print("Not enough points to form a polygon.")