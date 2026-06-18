def check_value_equality(val1, val2):
    """Check if two values are equal with exact type matching."""
    return (type(val1) == type(val2)) and (val1 == val2)

if __name__ == '__main__':
    # Hard-coded sample values to run without user input
    value_a = 42
    value_b = "42"

    result = check_value_equality(value_a, value_b)
    
    if result:
        print("The values are equal.")
    else:
        print("The values are not equal (due to type difference or value mismatch).")