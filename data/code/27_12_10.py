def check_inequality(a: float, b: float) -> bool:
    """
    Determines if two given floating-point numbers are unequal using standard comparison.

    While direct inequality operators (!=, != in boolean context of == ) work for floats,
    edge cases with extremely close values due to floating point representation can be tricky
    when exact bit-level difference is needed beyond mathematical expectation. However, the task
    specifies determining if they are "unequal", which typically implies standard mathematical inequality
    unless specified otherwise (e.g., checking if two measurements differ by more than a tolerance).

    This implementation uses Python's built-in '!=' operator for straightforward and performant comparison,
    as it is optimized in the CPython interpreter. For cases where an absolute difference epsilon check
    might be logically expected but not explicitly requested (like "strictly mathematically different"),
    we stick to direct inequality. Given constraints are minimal here.

    Parameters:
        a (float): First floating-point number.
        b (float): Second floating-point number.

    Returns:
        bool: True if the numbers are not equal, False otherwise.
    """
    return a != b

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    sample1 = 3.0
    sample2 = 4.0
    result_inequal_1 = check_inequality(sample1, sample2)

    sample3 = 5.5
    sample4 = float(5.5)
    # Note: In Python, creating a new int from float and back often preserves value exactly for simple cases
    # but binary floating point representation can differ slightly due to encoding nuances in some languages; 
    # however, standard == usually holds true here unless there is explicit epsilon discrepancy intended.
    
    result_inequal_2 = check_inequality(sample3, sample4)

    print(f"Is {sample1} != {sample2}? Result: {result_inequal_1}")  # Expected True
    print(f"Is {sample3} != {sample4}? Result: {result_inequal_2}")  # Expected False (they are equal numerically)

    sample5 = float('inf')
    sample6 = -float('inf')
    result_inequal_inf = check_inequality(sample5, sample6)
    print(f"Is inf != -inf? Result: {result_inequal_inf}")  # Expected True