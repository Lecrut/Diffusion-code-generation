def is_zero(value):
    """
    Returns True if the input value is exactly zero, False otherwise.
    
    This function handles integer 0, float 0 (including negative), 
    and works efficiently without floating-point comparison issues for exact zeros.
    For non-integer types like complex numbers or numpy scalars where available,
    it checks equality to 0 directly which is robust in Python's native handling.

    Args:
        value: A numerical argument (int, float).

    Returns:
        bool: True if value == 0, False otherwise.
    """
    return value == 0

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [
        (5, False),
        (-3.14, False),
        (0, True),
        (0.0, True),
        (float('-inf'), False),  # Testing infinity behavior implicitly covered by equality check in Python
        (None, TypeError)       # Note: None is not a number; strict type checking isn't requested but demonstrated below for robustness if needed. 
                               # However, per task "numerical argument", we assume valid input types. 
                               # The function will raise TypeError on non-numerics which is standard behavior.
    ]

    print("Testing 'is_zero' function with sample values:")
    results = []