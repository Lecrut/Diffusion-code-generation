import math

def is_within_tolerance(temp1: float, temp2: float) -> bool:
    """
    Check if the absolute difference between two temperature values 
    is within a predefined tolerance of 1 degree.
    
    Args:
        temp1 (float): First temperature value.
        temp2 (float): Second temperature value.
        
    Returns:
        bool: True if |temp1 - temp2| <= 1, False otherwise.
    """
    return abs(temp1 - temp2) <= 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (20.5, 21.3),   # Difference is 0.7 -> True
        (25.0, 26.9),   # Difference is 1.9 -> False
        (-5.2, -4.1),   # Difference is 1.1 -> False
        (0.0, 1.0),     # Exact difference of 1 -> True
    ]

    for t1, t2 in test_cases:
        result = is_within_tolerance(t1, t2)
        print(f"Temperature {t1} vs {t2}: {'Within tolerance' if result else 'Outside tolerance'}")