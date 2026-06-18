import math

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle given its radius using precise pi."""
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    samples = [0.5, 3.14, -2]

    print("Circle Area Calculations:")
    for r in samples:
        if r < 0:
            print(f"Radius {r} is invalid (radius cannot be negative).")
        else:
            area = calculate_circle_area(r)
            print(f"Radius: {r}, Area: {area:.4f}")