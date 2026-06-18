"""
Script to compare two floating-point numbers with epsilon handling.

This module defines a function that safely compares two floats by accounting 
for potential representation inaccuracies using an epsilon value. It also 
includes a main execution block with hard-coded sample values for testing.
"""

def is_greater(a: float, b: float, epsilon: float = 1e-9) -> bool:
    """
    Determine if floating-point number 'a' is strictly greater than 'b'.

    Direct comparison of floats can be unreliable due to binary representation 
    inaccuracies. This function uses a small tolerance (epsilon) to define 
    equality and strict inequality relative to that range.

    Args:
        a (float): The first floating-point number.
        b (float): The second floating-point number.
        epsilon (float, optional): A small value representing the threshold for 
            considering two numbers equal. Defaults to 1e-9.

    Returns:
        bool: True if 'a' is greater than 'b', False otherwise.
    """
    # If a is significantly larger than b by more than epsilon, it's strictly greater.
    return (a - b) > epsilon

def main():
    """
    Main execution block containing hard-coded sample values for testing 
    the comparison logic without any user input or external dependencies.
    """
    # Sample 1: Two distinct numbers where a is clearly larger
    val_a = 3.5
    val_b = 2.0
    
    # Sample 2: Numbers that are very close, potentially differing only by epsilon
    val_c = 1.0 + (1e-9) / 2
    val_d = 1.0

    print(f"Comparing {val_a} and {val_b}:")
    if is_greater(val_a, val_b):
        print(f"{val_a} is larger than {val_b}")
    else:
        print(f"{val_a} is not strictly larger than {val_b}")

    print(f"\nComparing {val_c} and {val_d}:")
    if is_greater(val_c, val_d):
        print(f"{val_c} is slightly larger than {val_d}")
    else:
        # Since the difference is within epsilon (or effectively zero in this context), 
        # it will not be considered strictly greater.
        print("The values are considered equal or {val_c} is not strictly larger.")

if __name__ == '__main__':
    main()