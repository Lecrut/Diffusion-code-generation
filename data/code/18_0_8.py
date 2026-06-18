def strictly_greater(a: int | float) -> bool | None:
    """
    Checks if a number is strictly greater than zero.
    
    Args:
        a (int | float): The number to check.
        
    Returns:
        bool or None: True if the number is strictly positive, False otherwise.
                      Returns None if input conversion fails.
    """
    try:
        num = float(a)
        return num > 0
    except (ValueError, TypeError):
        return None

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user interaction
    samples = [10.5, "invalid", -3, True]

    for val in samples:
        result = strictly_greater(val)
        
        if result is None:
            print(f"Input {val}: Conversion error or invalid type.")
        else:
            status_msg = "Strictly greater than zero." if result else "Not strictly greater than zero."
            print(f"Number {val}: {status_msg}")