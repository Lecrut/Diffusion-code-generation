def compare_lengths(a: float, b: float) -> tuple[float, str]:
    """
    Computes the absolute difference between two floating-point numbers
    and returns a tuple with the difference and a descriptive string.

    Args:
        a (float): First number representing length A.
        b (float): Second number representing length B.

    Returns:
        tuple[float, str]: 
            - The first element is the absolute difference between a and b.
            - The second element is a string indicating which value is greater or if they are equal.
    """
    diff = abs(a - b)
    
    if a > b:
        return (diff, f"Length A ({a}) is greater than Length B ({b}).")
    elif b > a:
        return (diff, f"Length B ({b}) is greater than Length A ({a}).")
    else:
        return (diff, "Both lengths are equal.")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    length_a = 10.5
    length_b = 7.2
    
    result_diff, result_desc = compare_lengths(length_a, length_b)
    
    print(f"Absolute difference: {result_diff}")
    print(result_desc)