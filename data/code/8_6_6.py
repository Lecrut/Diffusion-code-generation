import math

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle given its radius using math.pi."""
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    samples = [0.5, 3.14, -2]

    print("Area calculations:")
    for radius in samples:
        if radius < 0:
            print(f"Radius {radius} is invalid (cannot be negative).")
        else:
            area = calculate_circle_area(radius)
            print(f"Circle with radius {radius}: Area = {area:.6f}")