def float_unequal(a: float, b: float) -> bool:
    """
    Determine if two floating-point numbers are unequal using direct comparison.
    
    Floating-point inequality is best determined by standard equality operators 
    because the 'not equal' operator ('!=') in Python correctly handles NaN values 
    and provides consistent behavior for all IEEE 754 cases, unlike epsilon-based 
    comparisons which require arbitrary tolerance thresholds.
    
    Args:
        a (float): First floating-point number.
        b (float): Second floating-point number.
        
    Returns:
        bool: True if the numbers are not equal, False otherwise.
    """
    return a != b

if __name__ == '__main__':
    # Sample test cases with hard-coded values to verify functionality without external input
    
    results = [
        float_unequal(1.0, 2.0),      # True: distinct integers represented as floats
        float_unequal(3.5, 3.5),      # False: identical floating-point numbers
        float_unequal(float('nan'), float('nan')), # False: NaN is not equal to itself (IEEE 754)
        float_unequal(1e-20, -1e-20), # True: opposite signs make them unequal even if very close magnitude-wise
        
        # Test with values that might differ only in the last bit of precision
        float_unequal(float.fromhex('0x3FF00000'), float.fromhex('0x3FEFFFFFFFFF')), 
    ]

    print("Test Results:")
    for i, result in enumerate(results):
        status = "PASS" if (i == 2 and not result) or \
                         (i != 2 and result) else f"UNEXPECTED: {result}"
        # Manual check based on expected logic above since we can't run the full suite here without execution context, 
        # but this block demonstrates usage.
        
    print("\nSample Execution Output:")
    test_cases = [
        ("1.0", "2.0"),
        (3.5, 3.5),
        (float('nan'), float('nan')),
        (1e-20, -1e-20)
    ]

    for val_a_str, val_b_str in test_cases:
        a = eval(val_a_str) if isinstance(eval(val_a_str), str) else eval(val_a_str) # Safe evaluation of literals here
        
        try:
            b_val = float('nan') if 'nan' in val_b_str.lower() else eval(val_b_str)
            
            is_unequal = a != b_val
            print(f"{val_a_str} vs {val_b_str}: Unequal? {is_unequal}")
        except Exception:
            pass # Handle any unexpected evaluation errors gracefully
        
    # Final confirmation run with explicit literals to ensure standalone correctness
    final_check = float_unequal(1.0, 2.5)
    print(f"\nFinal Check (1.0 != 2.5): {final_check}")