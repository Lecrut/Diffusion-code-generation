"""
Script to compare two floating-point numbers handling inaccuracies via epsilon.

This module defines a function to safely determine which of two floats is larger,
accounting for potential representation errors inherent in binary floating-point arithmetic.
It uses a small tolerance value (epsilon) to define equality and ordering rather than strict inequality checks.

Usage: Run the script directly or import the `compare_floats` function from this module.
"""

def compare_floats(a: float, b: float, epsilon: float = 1e-9) -> str:
    """
    Compare two floating-point numbers using an absolute tolerance (epsilon).

    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        epsilon (float): A small positive value representing the acceptable difference for equality. Default is 1e-9.

    Returns:
        str: 'greater' if a > b, 'less' if a < b, or 'equal' if |a - b| <= epsilon.
    
    Note:
        This function avoids direct inequality comparisons (like `>`) which can fail due to 
        floating-point precision issues when dealing with values that are mathematically equal but not bitwise identical.
    """
    diff = abs(a - b)
    if diff < epsilon:
        return "equal"
    elif a > b:  # This check is safe here because we already ruled out equality within tolerance
        return "greater"
    else:
        return "less"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files.
    
    # Test Case 1: Clearly different numbers
    val_1 = 3.5
    val_2 = 4.0
    
    result_case_1 = compare_floats(val_1, val_2)
    print(f"Comparing {val_1} and {val_2}: Result is '{result_case_1}'")

    # Test Case 2: Numbers that are mathematically equal but may have representation differences (e.g., from float operations)
    # Using powers of 2 often results in exact binary representations, while others might not. 
    # Here we simulate a scenario where precision matters by adding small noise or using non-terminating decimals if converted manually.
    val_3 = 0.1 + 0.2
    val_4 = 0.3
    
    result_case_2 = compare_floats(val_3, val_4)
    print(f"Comparing {val_3} (approx 0.1+0.2) and {val_4}: Result is '{result_case_2}'")

    # Test Case 3: Identical values stored in variables
    val_5 = 7.89
    val_6 = 7.89
    
    result_case_3 = compare_floats(val_5, val_6)
    print(f"Comparing {val_5} and {val_6}: Result is '{result_case_3}'")

    # Test Case 4: Very close numbers near the epsilon threshold (using default epsilon=1e-9)
    val_7 = 1.0 + 2 * 1e-9 - 1e-9 / 2
    val_8 = 1.0
    
    result_case_4 = compare_floats(val_7, val_8)
    print(f"Comparing {val_7} and {val_8}: Result is '{result_case_4}'")

    # Test Case 5: Negative numbers with different magnitudes
    val_neg_a = -10.5
    val_neg_b = -9.2
    
    result_case_5 = compare_floats(val_neg_a, val_neg_b)
    print(f"Comparing {val_neg_a} and {val_neg_b}: Result is '{result_case_5}'")

    # Test Case 6: Negative numbers very close to each other (should be 'equal' or determined by epsilon logic correctly applied)
    val_close_neg = -10.0 + 2 * 1e-9 / 3
    val_exact_neg = -10.0
    
    result_case_6 = compare_floats(val_close_neg, val_exact_neg)
    print(f"Comparing {val_close_neg} and {val_exact_neg}: Result is '{result_case_6}'")

    # Final summary of the logic applied to these samples
    print("\nSummary:")
    print("- Direct float comparison can be unreliable due to binary representation.")
    print("- Using an epsilon (tolerance) ensures that values like 0.1 + 0.2 and 0.3 are treated as equal if their difference is negligible.")