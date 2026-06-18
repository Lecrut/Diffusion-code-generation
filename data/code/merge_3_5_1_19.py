def compare_lengths(a: float, b: float) -> tuple[str, str]:
    """
    Compares two floating-point numbers and returns a tuple indicating
    which length is greater, less, or equal.

    Args:
        a (float): First number representing a "length".
        b (float): Second number representing another "length".

    Returns:
        Tuple[str, str]: A pair of strings describing the comparison result.
            - ("greater", "<)") if a > b
            - ("less", ">")  if a < b
            - ("equal", "=") if a == b
    """
    # Use direct comparison operators as requested
    if a > b:
        return "greater", "<)"
    elif a < b:
        return "less", ">"
    else:
        return "equal", "="

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    val1 = 3.14
    val2 = 2.71
    
    result_greater, symbol_greater = compare_lengths(val1, val2)
    
    print(f"Comparing {val1} and {val2}:")
    print(f"{result_greter}, {symbol_greter}")