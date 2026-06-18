import sys

def compare_values(a: float | int, b: float | int) -> bool:
    """
    Compare two arbitrary numeric values (int or float).
    
    Returns True if a is not equal to b, False otherwise.
    Uses direct comparison which is efficient for standard Python types.
    
    Args:
        a: First numeric value.
        b: Second numeric value.
        
    Returns:
        Boolean indicating inequality (True) or equality (False).
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        ("int vs int", 10, 20),
        ("float vs float", 3.14, 2.71),
        ("mixed types", 5, 5.0),
        ("negative numbers", -100, -99),
    ]

    print("Testing numeric inequality comparison:")
    
    for label, val_a, val_b in test_cases:
        result = compare_values(val_a, val_b)
        status = "Inequal" if result else "Equal"
        print(f"{label}: {val_a} vs {val_b} -> {status}")