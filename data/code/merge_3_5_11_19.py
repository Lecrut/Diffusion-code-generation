def compare_lengths(a: float, b: float) -> tuple[float, str]:
    """
    Computes the absolute difference between two floating-point numbers
    and returns a string indicating which number is greater (or if they are equal).

    Args:
        a (float): First numeric value.
        b (float): Second numeric value.

    Returns:
        tuple[float, str]: A tuple containing the absolute difference 
                           and a descriptive string about the comparison result.
    """
    diff = abs(a - b)
    
    if a > b:
        greater_desc = f"{a} is greater than {b}"
    elif b > a:
        greater_desc = f"{b} is greater than {a}"
    else:
        greater_desc = "Both values are equal"

    return diff, greater_desc

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    val1 = 3.5
    val2 = 7.2
    
    result_diff, result_msg = compare_lengths(val1, val2)
    
    print(f"Absolute difference: {result_diff}")
    print(f"Comparison message: {result_msg}")