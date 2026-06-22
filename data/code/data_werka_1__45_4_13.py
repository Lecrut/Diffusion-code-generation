import math

def calculate_circle_area(diameter):
    if diameter <= 0:
        raise ValueError("Diameter must be a positive number.")
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    return area

def test_calculate_circle_area():
    test_cases = {
        "positive_diameter": {"diameter": 10, "expected": math.pi * 25},
        "zero_diameter": {"diameter": 0, "expected": ValueError},
        "negative_diameter": {"diameter": -5, "expected": ValueError}
    }
    
    for name, case in test_cases.items():
        try:
            result = calculate_circle_area(case["diameter"])
            assert math.isclose(result, case["expected"], rel_tol=1e-9), f"Test {name} failed"
        except Exception as e:
            assert isinstance(e, case["expected"]), f"Test {name} failed with unexpected exception"

if __name__ == '__main__':
    test_calculate_circle_area()
    print("All tests passed.")