def compare_lengths(length_a: float, length_b: float) -> tuple[float, str]:
    """
    Compares two floating-point numbers representing lengths.
    
    Args:
        length_a (float): The first length value.
        length_b (float): The second length value.
        
    Returns:
        A tuple containing the absolute difference between the lengths 
        and a string describing which length is greater or if they are equal.
    """
    diff = abs(length_a - length_b)
    
    if length_a > length_b:
        return (diff, f"{length_a} is greater than {length_b}")
    elif length_b > length_a:
        return (diff, f"{length_b} is greater than {length_a}")
    else:
        return (0.0, "Both lengths are equal")

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    val1 = 5.732
    val2 = 4.891
    
    result_diff, result_desc = compare_lengths(val1, val2)
    
    print(f"Difference: {result_diff}")
    print(f"Description: {result_desc}")