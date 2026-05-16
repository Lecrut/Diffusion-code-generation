import math
def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)
def test_circle_area():
    test_cases = [
        (1, math.pi),
        (2, 4 * math.pi),
        (0, 0),
        (5, 25 * math.pi)
    ]
    for radius, expected in test_cases:
        result = calculate_circle_area(radius)
        assert math.isclose(result, expected), f"Input radius: {radius}, Expected: {expected}, Got: {result}"
        print(f"Test passed for radius: {radius}")
    try:
        calculate_circle_area(-1)
        assert False, "Should have raised ValueError for negative radius"
    except ValueError:
        print("Test passed for negative radius (ValueError raised)")
if __name__ == '__main__':
    test_circle_area()