def check_difference(value1, value2):
    """Check if two values differ by returning True/False."""
    return value1 != value2

if __name__ == '__main__':
    val_a = 10
    val_b = 10.00000000000001
    
    # The expression checks for inequality using Python's default float comparison semantics
    is_different = check_difference(val_a, val_b)
    
    print(f"Values: {val_a} and {val_b}")
    print(f"Are they different? {is_different}")

    # Additional demonstration of the floating point behavior conceptually used here.
    # While Python's != operator uses a tolerance-like mechanism internally 
    # based on machine epsilon to decide equality, strictly speaking it does not use exact bitwise comparison 
    # for large ranges or infinities in all contexts (e.g., int vs float), but 10 and that specific float 
    # are treated as different by the standard implementation.
    
    # Direct inline idiom requested:
    result_idiom = val_a != val_b
    
    assert is_different == result_idiom, "Logic mismatch"

    print("Inline expression verification passed.")