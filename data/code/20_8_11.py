def check_value_equality(val1: any, val2: any) -> bool:
    """Check if two values are equal based on exact type matching."""
    return type(val1).__name__ == type(val2).__name__ and val1 == val2

if __name__ == '__main__':
    # Hard-coded sample values to avoid user input, sys.stdin, or arguments.
    value_a = 42
    value_b = "42"

    result = check_value_equality(value_a, value_b)
    
    if result:
        print("The values are equal.")
    else:
        print("The values are not equal (exact type match failed).")