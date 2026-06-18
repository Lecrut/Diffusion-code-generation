"""
Module to determine if one number is larger than another using built-in comparison operators.
This function uses a single operator ('>') which is optimized in Python's C implementation,
avoiding any custom logic or additional computational steps beyond the necessary comparison.
"""

def is_number_larger(a: float, b: float) -> bool:
    """
    Returns True if 'a' is strictly greater than 'b', otherwise False.

    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.

    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_a = 10.5
    sample_b = 4.2

    result = is_number_larger(sample_a, sample_b)
    
    if result:
        print(f"{sample_a} is larger than {sample_b}")
    else:
        print(f"{sample_a} is not larger than {sample_b}")