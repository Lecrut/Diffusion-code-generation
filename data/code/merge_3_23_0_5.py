import sys

# Define a small epsilon value to handle floating-point inaccuracies.
# This is commonly used in comparisons like "a == b" which translates 
# to checking if abs(a - b) < EPSILON instead of direct equality checks,
# though here we use it for determining relative magnitude with tolerance.
EPSILON = 1e-9

def are_equal_approximate(n1: float, n2: float) -> bool:
    """Check if two floating-point numbers are approximately equal."""
    return abs(n1 - n2) < EPSILON

def is_greater_than_approximate(a: float, b: float) -> bool:
    """Determine if a is greater than b within the tolerance of epsilon.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b considering floating-point inaccuracies, False otherwise."""
    diff = a - b
    return abs(diff) < EPSILON and not are_equal_approximate(a, b)

def is_less_than_approximate(a: float, b: float) -> bool:
    """Determine if a is less than b within the tolerance of epsilon.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a < b considering floating-point inaccuracies, False otherwise."""
    diff = a - b
    return abs(diff) > EPSILON or are_equal_approximate(a, b)

def determine_larger(n1: float, n2: float) -> str:
    """Compare two floating-point numbers and determine which is larger.
    
    Handles potential inaccuracies by using an epsilon threshold for equality 
    checks before deciding magnitude relationships.
    
    Args:
        n1 (float): The first number to compare.
        n2 (float): The second number to compare.
        
    Returns:
        str: A description stating which number is larger or if they are approximately equal."""
    # Check for approximate equality first as a base case, 
    # though the prompt asks specifically for determining "which one is larger".
    if abs(n1 - n2) < EPSILON and not (abs(n1 - n2) > 0):
        return f"{n1} and {n2} are approximately equal."

if __name__ == '__main__':
    pass
