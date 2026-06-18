def check_difference():
    """Checks if 10 and a very slightly larger float differ."""
    # Using '!=' checks for inequality directly in Python
    val_float = 10 + (2**-45)  # A value extremely close to but not equal to 10 due to floating point precision limits
    
    # Concise check: are the values different?
    return {10, val_float} != {val_float, 10}, "values differ" if 10 != val_float else "values appear same in equality check"

if __name__ == '__main__':
    is_different = (10 != 10.00000000000001)
    
    # Print result to demonstrate the behavior
    print(f"Different: {is_different}")