import math

def calculate_circle_area(radius: float) -> float:
    """
    Calculates the area of a circle given its radius using the value from math.pi.
    
    Args:
        radius (float): The radius of the circle, must be non-negative.
        
    Returns:
        float: The calculated area of the circle.
        
    Raises:
        ValueError: If the radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_radiuses = [3, 5.7, 1]
    
    for r in sample_radiuses:
        area = calculate_circle_area(r)
        print(f"Area of circle with radius {r}: {area}")