def check_equality(a: any, b: any) -> bool:
    """Check if two values are equal with exact type matching."""
    return a == b and type(a) is type(b)

if __name__ == '__main__':
    # Hard-coded sample values to avoid interactive prompts
    val1 = 42
    val2 = "42"

    result = check_equality(val1, val2)
    
    if result:
        print("The values are equal.")
    else:
        print("The values are not equal (either different value or mismatched type).")