import math
def calculate_circle_area(radius):
    return math.pi * radius**2
if __name__ == '__main__':
    test_cases = [
        (1, math.pi * 1**2),
        (2, math.pi * 2**2),
        (0, 0),
        (10, math.pi * 10**2),
        (0.5, math.pi * 0.5**2)
    ]
    all_passed = True
    for radius, expected in test_cases:
        result = calculate_circle_area(radius)
        tolerance = 1e-9
        if abs(result - expected) < tolerance:
            print(f"Test passed for radius: {radius}, Expected: {expected}, Got: {result}")
        else:
            print(f"Test failed for radius: {radius}, Expected: {expected}, Got: {result}")
            all_passed = False
    if all_passed:
        print("\nAll test cases passed successfully.")
    else:
        print("\nSome test cases failed.")