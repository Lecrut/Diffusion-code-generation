def check_equal_exact(a: any, b: any) -> bool:
    """
    Checks if two values are equal based on both value equality 
    AND exact type matching using direct comparison with type().
    
    Args:
        a (any): First input value.
        b (any): Second input value.
        
    Returns:
        bool: True if types and values match exactly, False otherwise.
    """
    return isinstance(a, type(b)) and a == b

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user interaction
    val1 = 42
    val2 = "42"

    result = check_equal_exact(val1, val2)
    
    if result:
        print("The values are equal with exact type matching.")
    else:
        print("The values are not equal due to a difference in type or value.")