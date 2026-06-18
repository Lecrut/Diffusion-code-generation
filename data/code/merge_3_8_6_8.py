import math

def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius using math.pi for precision.
    
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
    # Hard-coded sample values for testing without user input or external dependencies
    test_radii = [5.0, -3.0]  # Includes a negative value to trigger error handling
    
    print("Circle Area Calculations:")
    
    for radius in test_radii:
        try:
            area = calculate_circle_area(radius)
            print(f"Radius: {radius}, Area: {area}")
        except ValueError as e:
            print(f"Error calculating area for radius {radius}: {e}")