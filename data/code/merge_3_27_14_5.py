def check_difference():
    """Check if two float values are different using a tolerance."""
    val1 = 10
    val2 = 10.00000000000001
    
    # Use math.isclose to handle floating-point precision issues
    import math
    is_close = math.isclose(val1, val2)
    
    if not is_close:
        return True
    else:
        return False

if __name__ == '__main__':
    result = check_difference()
    print(f"Are 10 and {10.00000000000001} different? {result}")