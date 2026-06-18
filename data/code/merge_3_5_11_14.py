def compare_lengths(a: float, b: float) -> tuple[float, str]:
    """
    Computes the absolute difference between two floating-point numbers
    and returns a string indicating which number is greater (or if they are equal).

    Args:
        a (float): First input value.
        b (float): Second input value.

    Returns:
        tuple[float, str]: A tuple containing the absolute difference 
                           and a descriptive string about the comparison result.
    """
    diff = abs(a - b)
    
    if a > b:
        greater_str = f"{a} is greater than {b}"
    elif b > a:
        greater_str = f"{b} is greater than {a}"
    else:
        greater_str = "Both values are equal"

    return diff, greater_str

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    val1 = 3.5
    val2 = 7.2
    
    result_diff, result_desc = compare_lengths(val1, val2)
    
    print(f"Difference: {result_diff}")
    print(f"Comparison: {result_desc}")