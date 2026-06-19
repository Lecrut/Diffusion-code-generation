import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def test_calculate_circle_area():
    assert abs(calculate_circle_area(0) - 0) < 1e-9, "Test case 1 failed"
    assert abs(calculate_circle_area(1) - math.pi) < 1e-9, "Test case 2 failed"
    assert abs(calculate_circle_area(2.5) - (math.pi * 6.25)) < 1e-9, "Test case 3 failed"
    assert abs(calculate_circle_area(10) - (math.pi * 100)) < 1e-9, "Test case 4 failed"

if __name__ == '__main__':
    test_calculate_circle_area()
    print("All tests passed.")