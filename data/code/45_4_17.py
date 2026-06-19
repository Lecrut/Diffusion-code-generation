import math

def validate_diameter(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number.")

def calculate_circle_area(diameter):
    validate_diameter(diameter)
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

def test_calculate_circle_area():
    assert abs(calculate_circle_area(10) - (math.pi * 25)) < 1e-9, "Test case for diameter 10 failed"
    assert abs(calculate_circle_area(0) - 0) < 1e-9, "Test case for diameter 0 failed"
    try:
        calculate_circle_area(-5)
    except ValueError as e:
        assert str(e) == "Diameter must be a positive number", "Test case for negative diameter failed"

if __name__ == '__main__':
    diameter1 = 10
    area1 = calculate_circle_area(diameter1)
    print(f"The area of a circle with diameter {diameter1} is: {area1}")
    
    diameter2 = 0
    try:
        area2 = calculate_circle_area(diameter2)
        print(f"The area of a circle with diameter {diameter2} is: {area2}")
    except ValueError as e:
        print(f"Error: {e}")

    diameter3 = -5
    try:
        area3 = calculate_circle_area(diameter3)
        print(f"The area of a circle with diameter {diameter3} is: {area3}")
    except ValueError as e:
        print(f"Error: {e}")

    test_calculate_circle_area()
    print("All tests passed.")