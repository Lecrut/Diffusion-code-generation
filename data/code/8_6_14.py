import math

def calculate_circle_area(radius: float) -> float:
    """
    Calculates the area of a circle given its radius using math.pi.
    
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
    # Hard-coded sample values for testing without user input or network access
    test_cases = [3.14, -5, 0]

    print(f"Area of circle with radius {test_cases[0]}: {calculate_circle_area(test_cases[0])}")
    
    try:
        area_neg = calculate_circle_area(test_cases[1])
    except ValueError as e:
        print(f"Error for negative radius: {e}")

    zero_radius_area = calculate_circle_area(0)
    print(f"Area of circle with radius 0: {zero_radius_area}")