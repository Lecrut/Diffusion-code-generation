"""
Optimized algorithm to compare two temperature values within a predefined tolerance of 1 degree.
Returns True if the absolute difference is <= 1, otherwise False.
No user input or external dependencies required.
"""

def temperatures_within_tolerance(temp_a: float, temp_b: float) -> bool:
    """
    Check if the absolute difference between two temperature values is within 1 degree.

    Args:
        temp_a (float): First temperature value in any unit.
        temp_b (float): Second temperature value in the same unit as temp_a.

    Returns:
        bool: True if abs(temp_a - temp_b) <= 1, False otherwise.
    """
    return abs(temp_a - temp_b) <= 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    test_cases = [
        (20.5, 20.3),   # Difference is 0.2 -> Should return True
        (25.0, 26.1),   # Difference is 1.1 -> Should return False
        (-5.5, -4.9),   # Difference is 0.6 -> Should return True
        (30.0, 31.0),   # Difference is exactly 1.0 -> Should return True
    ]

    for i, (val_a, val_b) in enumerate(test_cases):
        result = temperatures_within_tolerance(val_a, val_b)
        print(f"Test case {i + 1}: compare {val_a} and {val_b}")
        print(f"Difference: {abs(val_a - val_b)}")
        print(f"Within tolerance (<= 1.0): {result}\n")