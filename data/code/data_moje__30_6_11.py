import math

def calculate_circle_area(radius):
    try:
        if not isinstance(radius, (int, float)):
            raise TypeError("Radius must be a numeric value")
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        return math.pi * radius * radius
    except Exception as e:
        return str(e)

def test_calculate_circle_area():
    test_cases = [
        (5, math.pi * 25),
        (0, 0),
        (-3, "Radius cannot be negative"),
        ("10", "Radius must be a numeric value"),
        (None, "Radius must be a numeric value"),
        ([1, 2], "Radius must be a numeric value"),
    ]
    results = []
    for radius, expected in test_cases:
        result = calculate_circle_area(radius)
        if isinstance(expected, float):
            match = abs(result - expected) < 1e-9
        else:
            match = result == expected
        results.append((radius, result, match))
    return results

if __name__ == '__main__':
    sample_radius = 5
    area = calculate_circle_area(sample_radius)
    print(area)

    test_results = test_calculate_circle_area()
    for radius, result, passed in test_results:
        print(f"Radius: {radius}, Result: {result}, Passed: {passed}")