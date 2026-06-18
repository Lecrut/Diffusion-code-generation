import math

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle given its radius using precise pi value."""
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_radius = 5.0
    
    try:
        result = calculate_circle_area(test_radius)
        print(f"Area of a circle with radius {test_radius}: {result}")
    except Exception as e:
        print(f"Error calculating area: {e}")