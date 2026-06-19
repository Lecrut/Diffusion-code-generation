import math

def calculate_circle_area(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number")
    radius = diameter / 2
    return math.pi * (radius ** 2)

def test_calculate_circle_area():
    try:
        assert abs(calculate_circle_area(10) - 78.53981633974483) < 1e-9, "Test case for diameter 10 failed"
        assert calculate_circle_area(0) == 0, "Test case for diameter 0 failed"
    except AssertionError as e:
        print(e)
    try:
        calculate_circle_area(-5)
    except ValueError as e:
        assert str(e) == "Diameter must be a positive number", "Test case for negative diameter failed"

if __name__ == '__main__':
    try:
        diameter1 = 10
        area1 = calculate_circle_area(diameter1)
        print(f"The area of a circle with diameter {diameter1} is: {area1}")
        diameter2 = 0
        area2 = calculate_circle_area(diameter2)
        print(f"The area of a circle with diameter {diameter2} is: {area2}")
        diameter3 = -5
        try:
            area3 = calculate_circle_area(diameter3)
            print(f"The area of a circle with diameter {diameter3} is: {area3}")
        except ValueError as e:
            print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

    test_calculate_circle_area()
    print("All tests passed.")