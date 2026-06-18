import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Uses math.pi for precision and returns the result as a float.
    
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
    # Hard-coded sample values to demonstrate functionality without external input
    test_cases = [3.5, 7]

    for radius in test_cases:
        area = calculate_circle_area(radius)
        print(f"Radius: {radius}")
        print(f"Area: {area:.2f}\n")