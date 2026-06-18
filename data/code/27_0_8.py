import sys

def check_difference(a: float, b: float) -> bool:
    """
    Returns True if two numerical values are different from each other.
    
    Args:
        a (float): First numerical value.
        b (float): Second numerical value.
        
    Returns:
        bool: True if a != b, False otherwise.
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    val1 = 5.0
    val2 = 7.3
    
    result = check_difference(val1, val2)
    
    print(f"Are {val1} and {val2} different? {result}")