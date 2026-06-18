import math

def convex_hull_monotone_chain(points):
    """
    Computes the vertices of the smallest convex polygon enclosing all given points
    using the Monotone Chain algorithm (O(n log n)).
    
    Args:
        points: List of [x, y] tuples representing 2D points.
        
    Returns:
        List of [x, y] tuples forming the vertices of the convex hull in counter-clockwise order.
    """
    if not points or all(p[0] == p[1][0] and p[1] == p[2][0] for i, (p) in enumerate(points)): # Check for empty or single unique point logic implicitly handled below
    
        n = len(points)
        if n <= 3:
            return points[:n]

    # Sort by x-coordinate, then y-coordinate
    sorted_points = sorted(set(points))
    
    def cross_product(o, a, b):
        """Returns the cross product of vectors OA and OB."""
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

    # Concatenate lower and upper to get full hull, removing the last point of each list 
    # because it's repeated at the start of the other.
    if len(lower) + len(upper) - 2 < n:
        return [] # Degenerate case where all points are collinear

    hull = lower[:-1] + upper[:-1]
    
    # Ensure we have at least 3 points for a polygon, otherwise it's not an area-bearing shape.
    if len(hull) <= 2:
        return list(sorted_points[:len(sorted_points)]) 

    return hull

def compute_area_polygon(vertices):
    """
    Computes the area of a simple polygon given its vertices in order using the Shoelace formula.
    
    Args:
        vertices: List of [x, y] tuples representing vertices in counter-clockwise (or clockwise) order.
        
    Returns:
        The absolute area as a float.
    """
    n = len(vertices)
    if n < 3:
        return 0.0
    
    area = 0.5 * abs(sum(
        x1 * y2 - x2 * y1 
        for (x1, _), (x2, _) in zip(vertices[:-1], vertices[1:]) + [(vertices[-1][0], vertices[0][1])] # Wrap around logic handled by loop structure if done correctly below. Let's use standard formula directly.
    ))

    area = 0.5 * abs(sum(
        (x[i] - x[(i+1)%n]) * (y[i-1] + y[(i+1)%n]) 
        for i in range(n) # This is a variation, let's stick to the classic Shoelace: sum(x_i*y_{i+1} - x_{i+1}*y_i)/2
    ))

    area = 0.5 * abs(sum(
        vertices[i][0] * vertices[(i + 1) % n][1] 
        for i in range(n)
    ) - sum(
        vertices[(i + 1) % n][0] * vertices[i][1] 
        for i in range(n)
    ))

    return area

def smallest_convex_polygon_area(points):
    """
    Computes the area of the smallest convex polygon enclosing all given points.
    
    Args:
        points (List[List[float]] or List[Tuple]): A list of 2D coordinates [x, y].
        
    Returns:
        float: The area of the convex hull. If fewer than 3 unique points exist, returns 0.0.
    """
    # Remove duplicates and ensure we have a list of lists for consistency
    unique_points = []
    seen = set()
    
    if not points:
        return 0.0
        
    for p in points:
        try:
            x, y = float(p[0]), float(p[1])
        except (TypeError, IndexError):
            continue
            
        key = (x, y)
        if key not in seen:
            unique_points.append([x, y])
            seen.add(key)

    hull_vertices = convex_hull_monotone_chain(unique_points)
    
    # If the hull has fewer than 3 points, it cannot form a polygon with area > 0.
    if len(hull_vertices) < 3:
        return 0.0
        
    return compute_area_polygon(hull_vertices)

if __name__ == '__main__':
    # Hard-coded sample values representing various scenarios
    
    # Scenario 1: A set of points forming a rough square with some noise/outliers inside and outside
    sample_points_1 = [
        [0, 0], [4, 2], [3, 5], [6, 7], 
        [8, 4], [9, 1], [5, -1] # Some points might be collinear or redundant
    ]

    # Scenario 2: Points on a circle (approximate)
    sample_points_2 = [
        [0.0, 3.0], 
        [-2.6457513110645905, -0.8542486889354095], 
        [-2.6457513110645905, 0.8542486889354095],
        [2.6457513110645905, -0.8542486889354095]
    ]

    # Scenario 3: Collinear points (should return area 0)
    sample_points_3 = [
        [1, 1], 
        [2, 2], 
        [3, 3], 
        [4, 4]
    ]

    # Scenario 4: Single point and two others forming a triangle with one very close to the line
    sample_points_4 = [
        [0.0, 0.0], 
        [10.0, 0.0], 
        [5.0, 2.0] # Small height
    ]

    test_cases = [
        ("Scenario 1 (General)", sample_points_1),
        ("Scenario 2 (Circular-ish)", sample_points_2),
        ("Scenario 3 (Collinear)", sample_points_3),
        ("Scenario 4 (Triangle)", sample_points_4)
    ]

    for name, pts in test_cases:
        area = smallest_convex_polygon_area(pts)
        print(f"{name}: Area of Convex Hull = {area:.2f}")