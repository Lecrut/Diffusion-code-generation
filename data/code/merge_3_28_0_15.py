def is_larger(a: float, b: float) -> bool:
    """
    Returns True if a is strictly larger than b, otherwise False.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b, False otherwise.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result1 = is_larger(5, 3)       # Expected: True
    result2 = is_larger(3, 5)       # Expected: False
    result3 = is_larger(4.7, 4.8)   # Expected: False
    
    print(f"is_larger({1}, {0}) -> {result1}")
    print(f"is_larger({2}, {5}) -> {result2}")
    print(f"is_larger({4.7}, {4.8}) -> {result3}")