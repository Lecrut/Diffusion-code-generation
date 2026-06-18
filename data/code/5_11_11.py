def compare_lengths(a: float, b: float) -> tuple[float, str]:
    """
    Compares two floating-point numbers and returns their absolute difference
    along with a description of which number is greater.

    Args:
        a (float): First input value representing length A.
        b (float): Second input value representing length B.

    Returns:
        tuple[float, str]: A tuple containing the absolute difference between 
                          the two values and a string indicating which one is larger.
                          If they are equal, it returns 'Equal'.
    """
    diff = abs(a - b)
    
    if a > b:
        greater_str = f"{a} is greater than {b}"
    elif b > a:
        greater_str = f"{b} is greater than {a}"
    else:
        greater_str = "Equal"

    return diff, greater_str

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    val1 = 5.7
    val2 = 3.2
    
    result_diff, result_desc = compare_lengths(val1, val2)
    
    print(f"Absolute difference: {result_diff}")
    print(f"Comparison description: {result_desc}")