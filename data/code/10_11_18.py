def compare_temperatures(temp_a: float | int, temp_b: float | int) -> str:
    """
    Compares two temperature values and returns a descriptive string.

    Args:
        temp_a (float | int): First temperature value.
        temp_b (float | int): Second temperature value.

    Returns:
        str: Description indicating relationship between temperatures.
    """
    # Using direct comparison is the most efficient approach for numerical values in Python,
    # leveraging C-level optimization behind float/int comparisons without overhead of library calls.
    
    if temp_a == temp_b:
        return f"Both temperatures are equal at {temp_a}."
    elif temp_a > temp_b:
        return f"{temp_a} is higher than {temp_b}."
    else:
        return f"{temp_a} is lower than {temp_b}."

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input.
    t1 = 25.5
    t2 = 30.0
    
    result = compare_temperatures(t1, t2)
    print(result)
    
    # Additional test cases inline for verification logic (not execution).
    assert compare_temperatures(20, 20) == "Both temperatures are equal at 20."
    assert compare_temperatures(-5.9, -4.1) == "-5.9 is lower than -4.1."
    assert compare_temperatures(float('inf'), float('-inf')) == f"{float('inf')} is higher than {float('-inf')}"