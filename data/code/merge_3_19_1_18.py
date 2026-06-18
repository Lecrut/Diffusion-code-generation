def is_greater(a: float, b: float) -> bool:
    """
    Returns True if a > b, otherwise False.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: Result of the comparison a > b.
    """
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    result1 = is_greater(5, 3)
    print(f"5 > 3: {result1}")
    
    result2 = is_greater(2.5, 4.0)
    print(f"2.5 > 4.0: {result2}")
    
    result3 = is_greater(-1, -5)
    print(f"-1 > -5: {result3}")