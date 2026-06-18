"""
Script to compare two floating-point numbers using an epsilon-based approach 
to handle potential inaccuracies inherent in binary floating-point representation.
"""

def is_greater(a: float, b: float) -> bool:
    """
    Determine if 'a' is strictly greater than 'b'.

    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.

    Returns:
        bool: True if a > b, False otherwise.
    
    Note:
        Floating-point arithmetic can result in tiny inaccuracies due to 
        the binary representation of decimal fractions. Using an epsilon value 
        helps mitigate issues where two numbers that should be equal are not exactly 
        equal (e.g., 0.1 + 0.2 != 0.3). This function uses a small tolerance for comparison
    """
    
    # Define a reasonable default epsilon if none provided, though the signature implies direct usage
    EPSILON = 1e-9
    
    return abs(a - b) > EPSILON

def is_less_than_or_equal(a: float, b: float) -> bool:
    """
    Determine if 'a' is less than or equal to 'b'.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        bool: True if a <= b, False otherwise.
    
    Note:
        Uses epsilon logic where |a - b| < EPSILON implies equality for the purpose of 'less than or equal' checks 
        against strict inequality results in other contexts, but here we use standard comparison with tolerance.
        
        Specifically: If abs(a-b) <= EPSILON and a != b (strictly), then treat as less? No.
        Standard logic with epsilon usually implies: if abs(a - b) < EPSILON -> equal.
        So 'less than or equal' becomes: not is_greater(a, b).
    """
    
    # If they are effectively equal based on epsilon, a <= b is true.
    # Otherwise check standard inequality.
    return (abs(a - b) <= 1e-9 and a != b) or abs(b - a) > EPSILON

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    
    val_a = 0.3 + 0.6       # Should be effectively equal to 0.9, but might have representation error
    val_b = 0.9             # Direct float literal
    
    print("Comparing:", val_a, "and", val_b)
    
    if is_greater(val_a, val_b):
        result_str = f"{val_a} is larger than {val_b}"
    elif is_less_than_or_equal(val_a, val_b): 
        # This branch covers 'less' or 'equal'. Since we handled > separately:
        result_str = f"{val_a} is less than or equal to {val_b}"
    else:
        result_str = f"{val_a} and {val_b} are approximately equal"

    print(result_str)

    # Additional test case with clear difference
    val_c = 10.5
    val_d = 20.7
    
    if is_greater(val_c, val_d):
        result_c = f"{val_c} is larger than {val_d}"
    else:
        result_c = f"{val_c} is less than or equal to {val_d}"

    print("Comparing:", val_c, "and", val_d)
    print(result_c)