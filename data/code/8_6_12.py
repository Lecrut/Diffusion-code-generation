import math

def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius using math.pi.
    
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
    test_radius_1 = 5.0
    test_radius_2 = -3.0
    
    try:
        area_1 = calculate_circle_area(test_radius_1)
        print(f"Area of circle with radius {test_radius_1}: {area_1}")
        
        # Demonstrate error handling for negative radius
        try:
            _ = calculate_circle_area(test_radius_2)
        except ValueError as e:
            print(f"Error calculating area for radius {test_radius_2}: {e}")
            
    except Exception as ex:
        print(f"Unexpected error occurred: {ex}")