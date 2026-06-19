import math

def calculate_circle_area(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number.")
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

def test_calculate_circle_area():
    try:
        assert abs(calculate_circle_area(10) - (math.pi * 25)) < 1e-9, "Test case for diameter 10 failed"
        assert abs(calculate_circle_area(0) - 0) < 1e-9, "Test case for diameter 0 failed"
    except AssertionError as e:
        print(f"AssertionError: {e}")
    try:
        calculate_circle_area(-5)
    except ValueError as e:
        assert str(e) == "Diameter must be a positive number.", "Test case for negative diameter failed"

if __name__ == '__main__':
    test_calculate_circle_area()
    print("All tests passed.")