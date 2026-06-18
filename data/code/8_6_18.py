import math

def calculate_circle_area(radius: float) -> float:
    """
    Calculates the area of a circle given its radius using math.pi for precision.
    
    Args:
        radius (float): The radius of the circle, must be non-negative.
        
    Returns:
        float: The calculated area of the circle.
    """
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    samples = [0, 1, 5, 3.14]
    
    print("Circle Area Calculations:")
    print("-" * 20)
    for r in samples:
        area = calculate_circle_area(r)
        print(f"Radius: {r} | Area: {area:.6f}")