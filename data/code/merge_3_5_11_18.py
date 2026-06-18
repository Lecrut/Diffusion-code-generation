def compare_lengths(a: float, b: float) -> tuple[float, str]:
    """
    Computes the absolute difference between two floating-point numbers 
    and returns a tuple with the difference and a description of which is greater.

    Args:
        a (float): First number representing length A.
        b (float): Second number representing length B.

    Returns:
        tuple[float, str]: A tuple containing the absolute difference and a string 
                           indicating whether 'a' or 'b' is larger if they are not equal.
    """
    diff = abs(a - b)
    
    if a > b:
        return (diff, f"Length {a} is greater than length {b}")
    elif b > a:
        return (diff, f"Length {b} is greater than length {a}")
    else:
        return (0.0, "Both lengths are equal")

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    sample_a = 10.5
    sample_b = 7.2
    
    difference, result_message = compare_lengths(sample_a, sample_b)
    
    print(f"Absolute Difference: {difference}")
    print(result_message)