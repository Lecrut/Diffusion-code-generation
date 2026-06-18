def check_values_equal(value1, value2):
    """Check if two values are exactly equal in both content and type."""
    return (value1 == value2) and (type(value1) is type(value2))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    val_a = 5
    val_b = 5
    
    result = check_values_equal(val_a, val_b)
    
    if result:
        print("The values are exactly equal in both content and type.")
    else:
        print("The values are not exactly equal or their types differ.")