import math

def convex_hull_monotone_chain(points):
    """
    Computes the vertices of the smallest enclosing convex polygon (Convex Hull) 
    using the Monotone Chain algorithm. This approach is O(n log n).
    
    Args:
        points (list[tuple[float, float]]): List of 2D coordinates [x, y].
        
    Returns:
        list[tuple[float, float]]: Vertices of the convex hull in counter-clockwise order.
    """
    # Remove duplicate points and sort by x-coordinate, then y-coordinate
    unique_points = sorted(list(set(points)))

    if len(unique_points) <= 1:
        return unique_points

    def cross_product(o, a, b):
        """Calculate the cross product of vectors OA and OB."""
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull
    lower = []
    for p in unique_points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(unique_points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    # Concatenate lower and upper to get full hull, removing the last point of each list 
    # because it's repeated in both (start/end node). If fewer than 3 unique points, handle gracefully.
    
    if len(unique_points) < 2:
        return []

    # Construct final hull without duplicating start and end nodes at the very beginning or end of combined lists unless needed for degenerate cases
    lower[:-1].extend(upper[1:-1])
    
    # If all points are collinear, Monotone Chain typically returns a list where first equals last. 
    # We keep it as is to represent the polygon path (point -> point), but strictly speaking, 
    # a "polygon" usually implies >2 vertices for area calculation if non-collinear.
    # For this function, we return the sequence of unique hull vertices starting from index 0 up to len-1.
    
    result = lower[:-1] + upper[1:-1]

    # If collinear points exist on the boundary that were included in 'lower' or 'upper', 
    # strictly convex hull might want only extreme points, but Monotone Chain with <= 0 cross product 
    # keeps intermediate points if they are not causing a turn. To ensure strict convexity (no three consecutive collinear),
    # we can re-evaluate turns using < 0 instead of <= 0 during construction for the hull shape itself? 
    # Actually, standard Monotone Chain with <= removes collinear intermediates automatically in subsequent steps if handled correctly,
    # but let's ensure strict convexity by checking cross product > 0. However, the prompt asks for smallest enclosing polygon.
    # If points are perfectly collinear, a polygon is degenerate (area 0). The standard implementation above handles this well 
    # enough to define the boundary line segments. We will stick to <= to remove collinear intermediate vertices if they don't create turns.

    return result

def convex_hull_area(points):
    """
    Computes the area of the smallest enclosing convex polygon using the computed hull coordinates.
    
    Args:
        points (list[tuple[float, float]]): List of 2D coordinates [x, y].
        
    Returns:
        float: Area of the convex polygon. If fewer than 3 unique points or all collinear, returns 0.0.
    """
    hull = convex_hull_monotone_chain(points)

    # A polygon needs at least 3 non-collinear vertices to have an area > 0 in a standard interpretation.
    if len(hull) < 3:
        return 0.0

    n = len(hull)
    
    # Shoelace formula for the sum of signed areas (closed polygon assumed by Monotone Chain order)
    double_area_x_sum = hull[0][0] * hull[1][1] - hull[1][0] * hull[0][1] + \
                        hull[n-1][0] * hull[n-2][1] - hull[n-2][0] * hull[n-1][1]

    double_area_y_sum = 0.0
    for i in range(n):
        j = (i + 1) % n
        x_i, y_i = hull[i]
        x_j, y_j = hull[j]
        
        # Contribution to the sum based on cross product logic relative to origin or just standard shoelace terms.
        # Standard Shoelace: Sum(x_i * y_{i+1} - x_{i+1} * y_i) for i from 0 to n-2 (since closed loop). 
        # Let's compute the full sum explicitly with modulo arithmetic logic or just iterate carefully.

    double_area = 0
    prev_x, prev_y = hull[0]
    
    for k in range(1, len(hull)):
        curr_x, curr_y = hull[k]
        
        double_area += (prev_x * curr_y - curr_x * prev_y)
        prev_x, prev_y = curr_x, curr_y
        
    # The area is half the absolute value of this sum. Since Monotone Chain returns counter-clockwise order 
    # for the upper + lower combination logic used here? Actually, standard implementation produces CCW if points are sorted by X then Y.
    
    return abs(double_area) / 2

if __name__ == '__main__':
    # Hard-coded sample values (list of tuples [x, y])
    sample_points = [
        (0.5, -1), 
        (-4.36, -9.87), 
        (.52, .45)
    ]

    result_area = convex_hull_area(sample_points)
    
    print(f"Input points: {sample_points}")
    print(f"Area of the smallest enclosing convex polygon: {result_area:.6f}")