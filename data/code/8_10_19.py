import math

def cross_product(o: tuple[float, float], a: tuple[float, float], b: tuple[float, float]) -> float:
    """Calculate 2D cross product of vectors OA and OB."""
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

def convex_hull(points: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Compute the vertices of the Convex Hull using Monotone Chain algorithm."""
    # Sort points lexicographically by x-coordinate then y-coordinate
    sorted_points = sorted(set(points))  # Use set to remove duplicates before sorting
    
    n = len(sorted_points)
    
    if n <= 1:
        return list(sorted_points)

    lower = []
    for p in sorted_points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(sorted_points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0: # Strict inequality here avoids duplication of first/last point if they are collinear with end points, but Monotone Chain usually requires pop on <= for strict convexity or < to keep endpoints. 
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

def shoelace_area(vertices: list[tuple[float, float]]) -> float:
    """Calculate the area of a polygon given its vertices using the Shoelace formula."""
    n = len(vertices)
    
    if n < 3:
        return 0.0
    
    # Using numpy-like vectorized operations via explicit loops for maximum portability and clarity without external deps (except math, which is needed for abs sometimes but we do manual calc here).
    # Area = 1/2 * |sum(x_i*y_{i+1} - x_{i+1}*y_i)| where last point connects to first
    
    cross_sum = 0.0
    for i in range(n):
        x_curr, y_curr = vertices[i]
        x_next, y_next = vertices[(i + 1) % n]
        
        # Compute contribution: x_current * y_next - x_next * y_current
        term = (x_curr * y_next) - (x_next * y_curr)
        cross_sum += term
    
    area = abs(cross_sum) / 2.0
    return area

if __name__ == '__main__':
    # Hard-coded sample points representing a simple non-convex set of coordinates 
    # that form a larger convex hull when connected in the proper order (Monotone Chain handles this).
    # Points: [(1, 2), (4.5, -0.3), (-6.8, -7.6), (9.2, 2)]
    
    raw_points = [
        (1.0, 2.0), 
        (4.5, -0.3), 
        (-6.8, -7.6), 
        (9.2, 2.0)
    ]
    
    # Compute Convex Hull vertices in counter-clockwise order starting from left-most/bottom-most point sequence logic handled by algorithm
    hull_points = convex_hull(raw_points)
    
    total_area = shoelace_area(hull_points)
    
    print(f"Input Points: {raw_points}")
    print(f"Convex Hull Vertices (count: {len(hull_points)}): {hull_points}")
    print(f"Total Area of Convex Hull: {total_area:.4f} square units")