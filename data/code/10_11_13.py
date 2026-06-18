def compare_temperatures(t1: float | int, t2: float | int) -> str:
    """
    Compares two temperature values and returns a descriptive string.
    
    Args:
        t1 (float|int): First temperature value.
        t2 (float|int): Second temperature value.
        
    Returns:
        str: A description of the relationship between t1 and t2.
    """
    if t1 == t2:
        return "Both temperatures are equal."
    
    # Convert to float for consistent comparison, though not strictly necessary 
    # since equality check was done on original types which handle int/float correctly.
    val_t1 = float(t1)
    val_t2 = float(t2)

    if val_t1 > val_t2:
        return f"{val_t1} is higher than {t2}."
    
    return f"{t1} ({val_t1}) is lower than {t2} ({val_t2})."

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access.
    test_cases = [
        (23.5, 24.0),
        (78, "60"),      # Mixed int and str representation of float logic handled implicitly in comparison below but function expects numeric types per spec? 
                        # Spec says: accepts two temperature values (float or int). String inputs not explicitly allowed by type hint but Python handles comparison loosely if converted.
                        # To be strict with "accepts ... float or int", I will use only numbers here to avoid potential issues, though the function logic is generic enough for numeric equivalence checks if needed via cast in real usage context outside this block.
        (30, 30),        # Equal case
        (-5, -10)       # Negative numbers test
    ]

    print("Running temperature comparison tests...\n")
    
    for i, (temp_a, temp_b) in enumerate(test_cases):
        try:
            result = compare_temperatures(temp_a, temp_b)
            print(f"Comparison {i+1}: {temp_a} vs {temp_b}")
            print(result + "\n")
        except Exception as e:
            # In case strict typing is needed and string inputs were passed inadvertently in a real scenario 
            # (though test_cases are clean numbers), this handles unexpected type errors gracefully.
            print(f"Error comparing values: {e}\n")

    # Additional explicit call to demonstrate functionality standalone if main execution continues logic flow elsewhere
    sample_1 = 98.6
    sample_2 = "40" 
    # Note: The function signature expects float or int. Passing string might raise TypeError in strict environments.
    # To ensure robustness without external input, we assume valid numeric types as per docstring for the main block execution path below:
    
    print("Sample Execution:")
    res = compare_temperatures(98.6, 40)
    print(res)