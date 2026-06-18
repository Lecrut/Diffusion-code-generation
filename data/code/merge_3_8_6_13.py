import math

def calculate_circle_area(radius: float) -> float:
    """Calculates the area of a circle given its radius using precise pi."""
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_cases = [0.5, 3, 10]
    
    print("Circle Area Calculations:")
    for r in test_cases:
        area = calculate_circle_area(r)
        print(f"Radius {r}: Area = {area:.2f}")