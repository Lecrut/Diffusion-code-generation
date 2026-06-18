import math

def are_close(a: float, b: float, rel_tol: float = 1e-9, abs_tol: float = 0.0) -> bool:
    """
    Compare two floating-point numbers for equality within a specified tolerance.
    
    This function uses relative and absolute tolerances to determine if two floats are 'close enough'.
    It leverages the math.isfinite() check implicitly by relying on standard comparison behavior,
    but explicitly checks finiteness first to avoid comparing NaN or infinity in edge cases 
    (though mathematical equality rules usually handle these differently).

    Parameters:
        a (float): First number.
        b (float): Second number.
        rel_tol (float): Relative tolerance - small value close to zero is preferred.
        abs_tol (float): Absolute tolerance - typically 0 but can be greater for special cases.

    Returns:
        bool: True if numbers are within the specified tolerances, False otherwise.
    
    The comparison logic follows: |a - b| <= max(rel_tol * max(|a|, |b|), abs_tol)
    """
    # Ensure both inputs are finite to avoid unexpected behavior with NaN or Infinity
    if not math.isfinite(a) and not math.isfinite(b):
        return False
    
    difference = a - b
    return (math.fabs(difference) <= max(rel_tol * max(abs(a), abs(b)), abs_tol))

if __name__ == '__main__':
    # Sample values for testing without any external input or file access.

    test_cases = [
        {"a": 1e-5, "b": 2e-5, "expected_false": True},      # Clearly different within tolerance usually? No wait, diff is > rel_tol * max(|a|, |b|) => False expected
        {
            "a": -1.0 / 3.0, 
            "b": float("-0.3333"), 
            "expected_false": True  
        },   # Floating point representation differences
    ]

    print("Running internal comparison tests...")
    
    for i, data in enumerate(test_cases):
        a = data["a"]
        b = data["b"]
        expected_true = not data.get("expected_false", False)  # Default to True if specified
        
        result = are_close(a, b)
        
        status_icon = "PASS" if bool(result) == expected_true else "FAIL"
        print(f"Test {i+1}: compare({a}, {b})")
        print(f"Result: {result}")
        print(f"Expected True/False: {expected_true}\n", file=__import__('sys').stderr, end="")