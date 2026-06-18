def compare_lengths(a: float, b: float) -> tuple[float, str]:
    """
    Computes the absolute difference between two floating-point numbers
    and returns a string indicating which number is greater.

    Args:
        a (float): First input value representing length A.
        b (float): Second input value representing length B.

    Returns:
        tuple[float, str]: A tuple containing the absolute difference 
                           and a descriptive string about which length is larger.
    """
    diff = abs(a - b)
    
    if a > b:
        return (diff, "Length A is greater")
    elif b > a:
        return (diff, "Length B is greater")
    else:
        return (diff, "Both lengths are equal")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    length_a = 10.5
    length_b = 7.2
    
    result_diff, result_desc = compare_lengths(length_a, length_b)
    
    print(f"Absolute difference: {result_diff}")
    print(f"Comparison description: {result_desc}")