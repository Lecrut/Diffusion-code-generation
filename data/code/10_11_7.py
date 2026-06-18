def compare_temperatures(temp1: float | int, temp2: float | int) -> str:
    """
    Compares two temperature values and returns a descriptive string.
    
    Args:
        temp1 (float|int): First temperature value.
        temp2 (float|int): Second temperature value.
        
    Returns:
        str: Description of the comparison result ('tempA is higher', 'tempB is lower', or 'equal').
             Format includes type names for clarity if different, otherwise just values and types combined.
    """
    # Determine which argument name to use based on order (simulating named arguments conceptually)
    arg1_name = "first"
    arg2_name = "second"

    is_equal = temp1 == temp2
    
    type_info_1 = f"{type(temp1).__name__} {temp1}" if isinstance(temp1, float) else str(temp1).replace(".0", "") + "°C (int)"
    
    # Check equality first for efficiency in cases where values might be large floats that aren't exactly equal but close? 
    # Actually direct comparison is standard and efficient enough.
    if temp1 == temp2:
        return f"{type_info_1} {arg1_name} temperature is equal to {temp2}°C"

    elif temp1 > temp2:
        type_str = "floats" if isinstance(temp1, float) else "ints" if isinstance(temp1, int) else "mixed"
        return f"{type_info_1} {arg1_name} temperature is higher than {temp2}°C ({type_str})"

    elif temp2 > temp1:
        type_str = "floats" if isinstance(temp2, float) else "ints" if isinstance(temp2, int) else "mixed"
        return f"{type_info_1} {arg1_name} temperature is lower than {temp2}°C ({type_str})"

    # Fallback (should not be reached due to early returns above for floats/ints logic unless complex types passed which are invalid per spec)

if __name__ == '__main__':
    # Hard-coded sample values running without user input or network access
    samples = [
        (25.0, 30),
        (-10, -10),
        (98.6, 72.5),
        (float('inf'), float('-inf')), 
        (42, 42) # Edge case for integers
    ]

    print("Running compare_temperatures with samples:\n")
    
    for i, vals in enumerate(samples):
        temp_a = vals[0]
        temp_b = vals[1]
        
        result = compare_temperatures(temp_a, temp_b)
        print(f"Test Case {i+1}: compare({temp_a}, {temp_b})")
        print(result)
        print("-" * 40)

    # Additional specific test for float equality edge case (e.g., .5 vs .50 representation if needed, though Python handles this well usually)
    special_float_test = (1.23456789, 1.23456789)
    result_special = compare_temperatures(*special_float_test)
    print(f"Special Float Test: {result_special}")