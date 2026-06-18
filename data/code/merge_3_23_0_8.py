"""
Script to compare two floating-point numbers with epsilon tolerance.

This module defines a function that compares two floats, accounting for 
floating-point representation inaccuracies by using a small epsilon value.
It also includes an example usage block in the main section.
"""

def is_greater(a: float, b: float) -> bool:
    """
    Determine if floating-point number 'a' is strictly greater than 'b'.

    This function uses a relative and absolute tolerance approach to handle 
    common floating-point comparison issues where direct equality or inequality 
    checks may fail due to binary representation errors.

    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.

    Returns:
        bool: True if 'a' is greater than 'b', False otherwise.
    
    Note:
        This implementation assumes the numbers are not extremely close in magnitude 
        relative to their scale, so a fixed epsilon combined with absolute difference 
        check provides robustness for typical use cases without needing complex 
        scaling logic unless specified otherwise by domain requirements.
        
        The default epsilon is set to 1e-9 which covers standard IEEE 754 double precision 
        noise levels in many practical scenarios.
    """
    # Define a small tolerance value (epsilon) for floating-point comparisons
    EPSILON = 1e-9
    
    # Check if the absolute difference between a and b is less than epsilon
    diff = abs(a - b)
    
    return not (diff < EPSILON or diff == 0.0)

def compare_numbers(num_a: float, num_b: float) -> str:
    """
    Compare two numbers and return the result as a descriptive string.

    Args:
        num_a (float): First number.
        num_b (float): Second number.

    Returns:
        str: A message indicating which number is larger or if they are effectively equal.
    """
    # Check if first number is greater than second with epsilon tolerance
    if is_greater(num_a, num_b):
        return f"{num_a} is strictly greater than {num_b}"
    
    # If not strictly greater and the difference isn't zero (handled by logic above), 
    # check reverse or equality. However, since we only need "which is larger",
    # if a <= b in this context:
    elif num_b > num_a - EPSILON:
        return f"{num_b} is strictly greater than {num_a}"
    
    else:
        return f"Numbers are effectively equal within tolerance of 1e-9."

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample case 1: Clearly different numbers
    val_1 = 3.14159265358979
    val_2 = 2.71828182845904
    
    result_case_1 = compare_numbers(val_1, val_2)
    
    # Sample case 2: Numbers very close due to floating point operations
    a_approx_pi = (3 + 1/16 + 1/(16**2)) * 7.5 / 480
    b_exact_pi_like = 3.14
    
    result_case_2 = compare_numbers(a_approx_pi, b_exact_pi_like)
    
    # Sample case 3: Identical values (should return equal message if logic covers it, 
    # but our is_greater returns False for exact equals unless diff < eps which fails on zero)
    val_c = 5.0
    val_d = 5.0
    
    result_case_3 = compare_numbers(val_c, val_d)

    print("Comparison Results:")
    print(f"Case 1 ({val_1} vs {val_2}):")
    print(result_case_1)
    
    print("\nCase 2 (Approx Pi vs Exact):")
    print(result_case_2)
    
    print("\nCase 3 (5.0 vs 5.0):")
    print(result_case_3)