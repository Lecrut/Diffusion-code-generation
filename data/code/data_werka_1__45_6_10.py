import math

def calculate_circle_area(radius):
    return math.pi * radius**2

if __name__ == '__main__':
    test_cases = {
        1: math.pi,
        2: 4 * math.pi,
        0: 0,
        5: 25 * math.pi,
        3.5: 12.25 * math.pi
    }
    for radius, expected in test_cases.items():
        result = calculate_circle_area(radius)
        tolerance = 1e-9
        if abs(result - expected) < tolerance:
            print(f"Test passed for radius: {radius}")
        else:
            print(f"Test failed for radius: {radius}, Expected: {expected}, Got: {result}")