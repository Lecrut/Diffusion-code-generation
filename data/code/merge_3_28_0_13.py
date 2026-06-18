def is_larger(a: float, b: float) -> bool:
    """
    Returns True if a is strictly larger than b, False otherwise.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if a > b, else False.
    """
    return a > b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    result1 = is_larger(5, 3)       # Expected: True
    result2 = is_larger(4, 4)       # Expected: False (equal)
    result3 = is_larger(-10.5, -9.7)# Expected: False (-10.5 < -9.7)
    
    print(f"is_larger({5}, {3}) = {result1}")   # True
    print(f"is_larger({4}, {4}) = {result2}")   # False
    print(f"is_larger(-10.5, {-9.7}) = {result3}")  # False
    
    assert result1 == True and result2 == False and result3 == False, "Test cases failed."