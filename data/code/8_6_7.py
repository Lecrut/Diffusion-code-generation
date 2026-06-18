import math

def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius using math.pi.
    
    Args:
        radius (float): The radius of the circle, must be non-negative.
        
    Returns:
        float: The calculated area of the circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_radii = [1, 5.5, 0]
    
    print(f"Area of circle with radius {test_radii[0]}: {calculate_circle_area(test_radii[0])}")
    print(f"Area of circle with radius {test_radii[1]}: {calculate_circle_area(test_radii[1])}")
    print(f"Area of circle with radius {test_radii[2]}: {calculate_circle_area(test_radii[2])}")