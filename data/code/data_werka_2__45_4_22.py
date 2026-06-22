import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

def test_calculate_circle_area():
    assert calculate_circle_area(0) == 0, "Area of circle with radius 0 should be 0"
    assert math.isclose(calculate_circle_area(1), math.pi), "Area of circle with radius 1 should be pi"
    assert math.isclose(calculate_circle_area(2.5), 19.634954084936208), "Area of circle with radius 2.5 should be approximately 19.635"
    assert math.isclose(calculate_circle_area(10), 314.1592653589793), "Area of circle with radius 10 should be approximately 314.159"

if __name__ == '__main__':
    test_calculate_circle_area()
    print("All tests passed.")