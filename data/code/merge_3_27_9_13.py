import sys

def compare_inequality(a: float | int, b: float | int) -> bool:
    """
    Compares two arbitrary numeric values (int or float).
    
    Returns True if a != b, False otherwise.
    Uses direct comparison which is efficient for standard Python types.
    
    Args:
        a: First numeric value.
        b: Second numeric value.
        
    Returns:
        Boolean indicating inequality status.
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files
    samples = [
        (1, 2),           # Integers
        (3.5, 4.0),       # Floats with different representations of same value if needed later
        (-10, -10),       # Negative integers equal
        (float('inf'), float('-inf')), # Infinity cases handled by standard comparison
    ]

    for i, (val_a, val_b) in enumerate(samples):
        result = compare_inequality(val_a, val_b)
        print(f"Sample {i+1}: a={val_a}, b={val_b} -> Inequality ({a != b}): {result}")