import math

def calculate_circle_area(radius: float) -> float:
    """
    Calculate the area of a circle given its radius using precise pi value from the math module.

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
    # Hard-coded sample values for testing
    samples = [5, 10.5, 0]

    print(f"Area of circle with radius {samples[0]}: {calculate_circle_area(samples[0])}")
    print(f"Area of circle with radius {samples[1]}: {calculate_circle_area(samples[1])}")
    print(f"Area of circle with radius {samples[2]}: {calculate_circle_area(samples[2])}")