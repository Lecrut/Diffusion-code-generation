def get_length_input(prompt):
    """Prompt the user (or use sample) to input a length measurement."""
    # Since we cannot call input() in this specific constraint set, 
    # this function is designed to be called by main which handles the logic.
    pass

if __name__ == '__main__':
    # Hard-coded sample values as per instructions (no user interaction)
    length_a = 10.5
    length_b = 23.7

    print("Comparison of Length Measurements")
    print(f"Value A: {length_a}")
    print(f"Value B: {length_b}")

    # Calculate difference
    diff = length_a - length_b
    
    if abs(diff) < 0.01: 
        print("\nDifference is negligible.")
    else:
        print(f"\nCalculated Difference (A - B): {diff:.2f}")
        
        if diff > 0:
            print("Value A is greater than Value B.")
        elif diff < 0:
            print("Value B is greater than Value A.")
        else:
            print("Values are equal.")

    # Validation simulation (since no actual input() call allowed)
    try:
        float(length_a)
        float(length_b)
        print("\nInput validation passed for sample values.")
    except ValueError as e:
        print(f"\nValidation failed with error: {e}")