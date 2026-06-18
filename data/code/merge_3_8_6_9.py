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
    sample_radius = 5.0
    area_result = calculate_circle_area(sample_radius)
    print(f"Area of a circle with radius {sample_radius}: {area_result}")