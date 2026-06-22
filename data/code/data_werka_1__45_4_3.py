import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def test_calculate_circle_area():
    assert abs(calculate_circle_area(0) - 0) < 1e-9, "Test case for radius 0 failed"
    assert abs(calculate_circle_area(1) - math.pi) < 1e-9, "Test case for radius 1 failed"
    assert abs(calculate_circle_area(2.5) - (math.pi * 6.25)) < 1e-9, "Test case for radius 2.5 failed"
    assert abs(calculate_circle_area(3) - (math.pi * 9)) < 1e-9, "Test case for radius 3 failed"

if __name__ == '__main__':
    test_calculate_circle_area()
    print("All tests passed.")