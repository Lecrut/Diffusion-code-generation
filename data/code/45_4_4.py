import math

def calculate_circle_area(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number.")
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

def test_calculate_circle_area():
    test_cases = {
        "diameter_1": {"diameter": 10, "expected": math.pi * (5 ** 2)},
        "diameter_2": {"diameter": 0, "expected": None},
        "diameter_3": {"diameter": -5, "expected": None},
    }
    
    for name, case in test_cases.items():
        try:
            result = calculate_circle_area(case["diameter"])
            assert math.isclose(result, case["expected"], rel_tol=1e-9), f"Test {name} failed: expected {case['expected']}, got {result}"
        except ValueError:
            if case["expected"] is not None:
                raise AssertionError(f"Test {name} failed: expected no exception for diameter {case['diameter']}")

if __name__ == '__main__':
    test_calculate_circle_area()
    print("All tests passed.")