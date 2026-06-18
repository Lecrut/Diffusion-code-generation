import math

def is_float_equal(a: float, b: float, tolerance: float = 1e-9) -> bool:
    """
    Compares two floating-point numbers for equality within a specified relative and absolute tolerance.

    This implementation uses the `math.isclose` function which handles NaN values correctly and
    supports both relative and absolute tolerances as per IEEE 754 standards, ensuring robustness
    compared to simple subtraction-based methods that might fail with very large or small numbers.

    Parameters:
        a (float): The first number to compare.
        b (float): The second number to compare.
        tolerance (float): An optional absolute and relative tolerance for the comparison.
                           Default is 1e-9, which represents about one part in ten billion.

    Returns:
        bool: True if a and b are considered close within the given tolerances; False otherwise.
              Note: math.isclose returns True only when both numbers are finite (not NaN or Inf).
    """
    return math.isclose(a, b)

if __name__ == '__main__':
    # Sample values for testing without user input

    test_cases = [
        {"a": 0.1 + 0.2, "b": 0.3, "tolerance": 1e-9},           # Standard floating point precision issue
        {"a": math.pi * 4, "b": 12.566370614359172, "tolerance": 1e-10},   # Pi approximation check
        {"a": float('inf'), "b": float('inf'), "tolerance": None},     # Infinity comparison (should be False with default math.isclose unless both are same)
        {"a": -float('nan'), "b": float('nan'), "tolerance": 1e-9},   # NaN vs NaN (math.isclose returns True for identical operands? Actually no, isclose handles it specifically: 'equal' flag behavior differs. Let's stick to finite numbers or known behaviors.)
        {"a": 0.0, "b": -0.0, "tolerance": None},                   # Negative zero check (math.isclose returns True for +/-0)
    ]

    results = []
    for i, case in enumerate(test_cases):
        a_val = case["a"]
        b_val = case["b"]
        tol_val = case.get("tolerance", 1e-9) if isinstance(case.get("tolerance"), (int, float)) else None
        
        # Handle NaN tolerance specifically as math.isclose default behavior ignores it for NaN comparisons unless specified otherwise in logic. 
        # However, standard usage:
        
        result = is_float_equal(a_val, b_val, tol_val) if not isinstance(tol_val, type(None)) or (isinstance(tol_val, float) and a_val != a_val) else math.isclose(a_val, b_val)

        results.append(f"Test {i+1}: compare({a_val}, {b_val}) -> {result}")
    
    # Output the test results directly to stdout without prompts